"""
Prediction Engine
"""
import pandas as pd
from typing import Dict, Any

from ml_backend.model_loader import (
    load_model,
    load_scaler,
    load_feature_columns
)

from ml_backend.explainability import (
    get_top_features,
    get_top_feature_importance,
    explain_prediction
)

from ml_backend.recommendations import (
    get_risk_level,
    get_recommendations
)


def get_feature_importance(model_name: str = "random_forest", top_n: int = 20):
    """
    Return feature importances in canonical list-of-dicts format (ordered).

    Example:
    [ {"feature": "Age", "importance": 0.123}, ... ]
    """
    return get_top_features(model_name=model_name, top_n=top_n)


def preprocess_customer_data(customer_data: Dict[str, Any]):
    """
    Preprocess a single customer record (dict) into the numeric feature array
    expected by the models. Uses `load_scaler()` and `load_feature_columns()`.

    Returns: numpy array (2D) ready for model.predict / predict_proba
    """
    if not isinstance(customer_data, dict):
        raise TypeError("customer_data must be a dict representing one customer")

    scaler = load_scaler()
    columns = load_feature_columns()

    df = pd.DataFrame([customer_data])
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)

    return scaler.transform(df)


def predict_single_customer(customer_data: Dict[str, Any], model_name: str = "random_forest") -> Dict[str, Any]:
    """
    Predict churn for a single customer record.

    Returns a dict with keys:
      - prediction: int (0/1)
      - probability: float (percentage 0-100, rounded to 2 decimals)
      - risk_level: str
      - top_factors: list (list-of-dicts canonical format)
      - explanations: list of strings
      - recommendations: list of strings
    """
    model = load_model(model_name)

    processed = preprocess_customer_data(customer_data)

    # model.predict expects 2D array
    preds = model.predict(processed)
    prediction = int(preds[0])

    # predict_proba may not be available for all models; prefer safe access
    probability = 0.0
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(processed)
        # assume positive class at index 1
        probability = float(proba[0][1])

    probability_percent = round(probability * 100, 2)

    top_factors = get_top_feature_importance(customer_data, top_n=5, model_name=model_name)

    explanations = explain_prediction(customer_data)

    recommendations = get_recommendations(probability_percent)

    return {
        "prediction": prediction,
        "probability": probability_percent,
        "risk_level": get_risk_level(probability_percent),
        "top_factors": top_factors,
        "explanations": explanations,
        "recommendations": recommendations
    }


def predict_batch(df: pd.DataFrame, model_name: str = "random_forest") -> pd.DataFrame:
    """
    Accepts a DataFrame of customer records, runs preprocessing and batch
    prediction, and returns an enriched DataFrame with appended columns:

      - Predicted_Churn       (int)
      - Churn_Probability     (float percentage 0-100)
      - Risk_Level            (str)

    This function uses `load_scaler()` and `load_feature_columns()` to
    align columns consistently with training artifacts.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("predict_batch expects a pandas DataFrame")

    model = load_model(model_name)
    scaler = load_scaler()
    columns = load_feature_columns()

    df_copy = df.copy()

    # Preprocess: dummies and reindex to feature columns
    processed = pd.get_dummies(df_copy)
    processed = processed.reindex(columns=columns, fill_value=0)

    # Scale
    X = scaler.transform(processed)

    # Predict
    preds = model.predict(X)

    probabilities = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X)
        # take positive-class probability
        probabilities = [float(p[1]) for p in proba]
    else:
        # If model has no predict_proba, fallback to zeros
        probabilities = [0.0 for _ in preds]

    # Append results
    df_copy["Predicted_Churn"] = [int(p) for p in preds]
    df_copy["Churn_Probability"] = [round(p * 100, 2) for p in probabilities]
    df_copy["Risk_Level"] = [get_risk_level(round(p * 100, 2)) for p in probabilities]

    return df_copy
