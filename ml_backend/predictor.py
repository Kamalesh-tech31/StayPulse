"""
Main Prediction Entry Point
"""
from ml_backend.prediction_engine import (
    predict_single_customer,
    predict_batch,
    get_feature_importance
)


def predict_churn(customer_data, model_name="random_forest"):
    """
    Predict churn for a single customer.

    Delegates to `ml_backend.prediction_engine.predict_single_customer`.

    Input:
      - customer_data: dict representing a single customer
      - model_name: optional model name string (default "random_forest")

    Returns: dict as returned by `predict_single_customer`.
    """
    return predict_single_customer(customer_data, model_name)


def predict_dataset(df, model_name="random_forest"):
    """
    Predict churn for a batch of customers.

    Delegates to `ml_backend.prediction_engine.predict_batch`.

    Input:
      - df: pandas DataFrame with customer records
      - model_name: optional model name string (default "random_forest")

    Returns: pandas DataFrame enriched with prediction columns.
    """
    return predict_batch(df, model_name)


def get_model_feature_importance(model_name="random_forest"):
    """
    Return model feature importances in canonical list-of-dicts format.

    Delegates to `ml_backend.prediction_engine.get_feature_importance`.

    Input:
      - model_name: optional model name string (default "random_forest")

    Returns: list of {"feature": name, "importance": float}
    """
    return get_feature_importance(model_name=model_name)