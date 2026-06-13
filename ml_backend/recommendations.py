"""
Recommendation Engine
"""


def get_risk_level(
    probability
):

    if probability >= 70:
        return "High"

    if probability >= 40:
        return "Medium"

    return "Low"


def get_recommendations(
    probability
):

    risk = get_risk_level(
        probability
    )

    if risk == "High":

        return [
            "Immediate retention campaign",
            "Assign relationship manager",
            "Offer loyalty incentives"
        ]

    if risk == "Medium":

        return [
            "Send engagement campaign",
            "Promote additional banking products"
        ]

    return [
        "Maintain current engagement strategy"
    ]


def generate_customer_strategy(
    prediction_result
):

    probability = prediction_result[
        "probability"
    ]

    return {
        "risk_level":
        get_risk_level(probability),

        "recommendations":
        get_recommendations(probability)
    }