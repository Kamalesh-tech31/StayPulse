"""
Model Explainability
"""

from ml_backend.model_loader import (
    load_model,
    load_feature_columns
)


def get_feature_importance(
    model_name="random_forest"
):

    model = load_model(model_name)

    columns = load_feature_columns()

    if not hasattr(
        model,
        "feature_importances_"
    ):
        return []

    features = []

    for feature, score in zip(
        columns,
        model.feature_importances_
    ):

        features.append({
            "feature": feature,
            "importance": float(score)
        })

    features.sort(
        key=lambda x: x["importance"],
        reverse=True
    )

    return features


def get_top_features(model_name="random_forest", top_n=5):
    """
    Return the top `top_n` features by importance for the specified model.

    This is a thin wrapper around `get_feature_importance()` that enforces
    the canonical list-of-dicts format and returns only the top N items.
    """
    importances = get_feature_importance(model_name)

    if not importances:
        return []

    try:
        n = int(top_n)
    except Exception:
        n = 0

    if n <= 0:
        return []

    return importances[:n]


def get_top_feature_importance(
    customer_data,
    top_n=5,
    model_name="random_forest"
):
    """
    Returns only important active features
    for a customer
    """

    importances = get_feature_importance(
        model_name
    )

    factors = []

    for item in importances:

        feature = item["feature"]

        if feature in customer_data:

            value = customer_data[
                feature
            ]

            if value not in [0, None, ""]:

                factors.append({
                    "feature": feature,
                    "importance":
                    item["importance"]
                })

    if not factors:

        return importances[:top_n]

    return factors[:top_n]


def explain_prediction(
    customer_data
):

    explanations = []

    if customer_data.get(
        "Age",
        0
    ) >= 50:

        explanations.append(
            "Customer belongs to higher churn age group"
        )

    if customer_data.get(
        "NumOfProducts",
        2
    ) <= 1:

        explanations.append(
            "Low product adoption"
        )

    if customer_data.get(
        "IsActiveMember",
        1
    ) == 0:

        explanations.append(
            "Inactive customer"
        )

    if customer_data.get(
        "Balance",
        0
    ) > 100000:

        explanations.append(
            "High account balance"
        )

    return explanations