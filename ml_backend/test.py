from ml_backend.predictor import (
    predict_churn
)

sample = {

    "CreditScore": 450,
    "Geography": "France",
    "Gender": "Male",
    "Age": 60,
    "Tenure": 2,
    "Balance": 150000,
    "NumOfProducts": 1,
    "HasCrCard": 1,
    "IsActiveMember": 0,
    "EstimatedSalary": 50000
}

print(
    predict_churn(
        sample
    )
)