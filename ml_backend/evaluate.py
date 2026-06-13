from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


def evaluate_model(
    model,
    X_test,
    y_test
):

    predictions = model.predict(X_test)

    print(
        f"Accuracy : {accuracy_score(y_test, predictions):.4f}"
    )

    print(
        f"Precision : {precision_score(y_test, predictions):.4f}"
    )

    print(
        f"Recall : {recall_score(y_test, predictions):.4f}"
    )

    print(
        f"F1 Score : {f1_score(y_test, predictions):.4f}"
    )

    print("\nClassification Report:\n")

    print(
        classification_report(
            y_test,
            predictions
        )
    )

    print("\nConfusion Matrix:\n")

    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )