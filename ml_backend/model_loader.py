from pathlib import Path

import joblib


MODELS_DIR = Path(__file__).parent / "models"


def load_model(model_name="random_forest"):

    if model_name == "random_forest":
        return joblib.load(
            MODELS_DIR / "random_forest_model.pkl"
        )

    if model_name == "logistic":
        return joblib.load(
            MODELS_DIR / "logistic_model.pkl"
        )

    raise ValueError(
        f"Unknown model: {model_name}"
    )


def load_scaler():

    return joblib.load(
        MODELS_DIR / "scaler.pkl"
    )


def load_feature_columns():

    return joblib.load(
        MODELS_DIR / "columns.pkl"
    )