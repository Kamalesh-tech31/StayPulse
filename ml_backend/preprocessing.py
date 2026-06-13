import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data(path):
    """
    Load dataset from CSV file
    """
    return pd.read_csv(path)


def clean_data(df):
    """
    Remove unnecessary columns
    """
    return df.drop(
        ["RowNumber", "CustomerId", "Surname"],
        axis=1
    )


def create_features(df):
    """
    Feature engineering
    """

    # Age buckets
    df["AgeGroup"] = pd.cut(
        df["Age"],
        bins=[0, 30, 50, 100],
        labels=["Young", "Middle", "Senior"]
    )

    # Customer engagement
    df["EngagementScore"] = (
        df["HasCrCard"] +
        df["IsActiveMember"]
    )

    # Balance vs Salary
    df["BalanceSalaryRatio"] = (
        df["Balance"] /
        (df["EstimatedSalary"] + 1)
    )

    # Products relative to tenure
    df["ProductsPerTenure"] = (
        df["NumOfProducts"] /
        (df["Tenure"] + 1)
    )

    # Customer value
    df["CustomerValue"] = (
        df["Balance"] *
        df["NumOfProducts"]
    )

    return df


def encode_features(df):
    """
    Convert categorical variables
    """
    return pd.get_dummies(
        df,
        drop_first=True
    )


def split_features_target(df):

    X = df.drop("Exited", axis=1)
    y = df["Exited"]

    return X, y


def scale_features(X_train, X_test):

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    joblib.dump(
        scaler,
        "ml_backend/models/scaler.pkl"
    )

    return X_train, X_test


def preprocess_pipeline(path):

    df = load_data(path)

    df = clean_data(df)

    df = create_features(df)

    df = encode_features(df)

    feature_columns = df.drop(
        "Exited",
        axis=1
    ).columns

    joblib.dump(
        feature_columns,
        "ml_backend/models/columns.pkl"
    )

    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    X_train, X_test = scale_features(
        X_train,
        X_test
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )