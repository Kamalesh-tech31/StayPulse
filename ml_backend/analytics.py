"""
Analytics Module
Business and model analytics
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

import pandas as pd


def calculate_model_metrics(model, X_test, y_test):

    predictions = model.predict(X_test)

    return {
        "accuracy": round(
            accuracy_score(y_test, predictions), 4
        ),
        "precision": round(
            precision_score(y_test, predictions), 4
        ),
        "recall": round(
            recall_score(y_test, predictions), 4
        ),
        "f1_score": round(
            f1_score(y_test, predictions), 4
        )
    }


def get_confusion_matrix_data(
    model,
    X_test,
    y_test
):
    predictions = model.predict(X_test)

    return confusion_matrix(
        y_test,
        predictions
    )


def churn_distribution(df):

    total = len(df)

    churned = int(df["Exited"].sum())

    retained = total - churned

    return {
        "total_customers": total,
        "churned": churned,
        "retained": retained,
        "churn_rate": round(
            churned / total * 100,
            2
        )
    }


def revenue_at_risk(df):

    if (
        "Churn_Probability" not in df.columns
        or "Balance" not in df.columns
    ):
        return 0

    risk = (
        df["Churn_Probability"] / 100
        * df["Balance"]
    ).sum()

    return round(risk, 2)