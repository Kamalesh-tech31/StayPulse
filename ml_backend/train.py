import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

from ml_backend.preprocessing import preprocess_pipeline
from ml_backend.evaluate import evaluate_model


def train_models():

    # Load processed data
    X_train, X_test, y_train, y_test = preprocess_pipeline(
        "dataset/Churn_Modelling.csv"
    )

    print("Training Logistic Regression...")

    logistic_model = LogisticRegression(
        class_weight="balanced",
        max_iter=1000,
        random_state=42
    )

    logistic_model.fit(X_train, y_train)

    print("Training Random Forest...")

    rf = RandomForestClassifier(
        random_state=42,
        class_weight="balanced"
    )

    param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [10, 15, 20, None],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    }

    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        cv=5,
        scoring="f1",
        n_jobs=-1,
        verbose=1
    )

    grid_search.fit(X_train, y_train)

    best_rf = grid_search.best_estimator_

    print("\nBest RF Parameters:")
    print(grid_search.best_params_)

    # Save models
    joblib.dump(
        logistic_model,
        "ml_backend/models/logistic_model.pkl"
    )

    joblib.dump(
        best_rf,
        "ml_backend/models/random_forest_model.pkl"
    )

    print("\n" + "=" * 50)
    print("LOGISTIC REGRESSION")
    print("=" * 50)

    evaluate_model(
        logistic_model,
        X_test,
        y_test
    )

    print("\n" + "=" * 50)
    print("RANDOM FOREST")
    print("=" * 50)

    evaluate_model(
        best_rf,
        X_test,
        y_test
    )


if __name__ == "__main__":
    train_models()