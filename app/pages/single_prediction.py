import streamlit as st

from ml_backend.predictor import predict_churn


def render_single_prediction():
    st.title("Single Customer Prediction")
    st.subheader("Analyze a single customer and generate explainable churn predictions")
    st.markdown("---")

    st.markdown("Fill the customer fields below and click **Analyze Customer**.")

    with st.form(key="customer_form"):
        CreditScore = st.number_input("Credit Score", min_value=300, max_value=850, value=450, step=1)
        Geography = st.selectbox("Geography", options=["France", "Spain", "Germany"], index=0)
        Gender = st.selectbox("Gender", options=["Male", "Female"], index=0)
        Age = st.number_input("Age", min_value=18, max_value=100, value=60, step=1)
        Tenure = st.number_input("Tenure", min_value=0, max_value=10, value=2, step=1)
        Balance = st.number_input("Balance", min_value=0.0, value=150000.0, step=100.0, format="%.2f")
        NumOfProducts = st.number_input("Num Of Products", min_value=1, max_value=10, value=1, step=1)
        HasCrCard = st.selectbox("Has Credit Card", options=["Yes", "No"], index=0)
        IsActiveMember = st.selectbox("Is Active Member", options=["Yes", "No"], index=1)
        EstimatedSalary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0, step=100.0, format="%.2f")

        submit = st.form_submit_button("Analyze Customer")

    if submit:
        customer_data = {
            "CreditScore": int(CreditScore),
            "Geography": Geography,
            "Gender": Gender,
            "Age": int(Age),
            "Tenure": int(Tenure),
            "Balance": float(Balance),
            "NumOfProducts": int(NumOfProducts),
            "HasCrCard": 1 if HasCrCard == "Yes" else 0,
            "IsActiveMember": 1 if IsActiveMember == "Yes" else 0,
            "EstimatedSalary": float(EstimatedSalary),
        }

        st.subheader("Prediction in progress...")

        try:
            result = predict_churn(customer_data)
        except Exception as e:
            st.error(f"Prediction failed: {e}")
        else:
            st.subheader("Prediction Result")
            st.write("**Predicted Churn (0 = stay, 1 = churn):**", result.get("prediction"))

            st.subheader("Churn Probability")
            st.write(f"{result.get('probability')} %")

            st.subheader("Risk Level")
            st.write(result.get("risk_level"))

            st.subheader("Top Factors")
            top_factors = result.get("top_factors") or []
            if isinstance(top_factors, list) and top_factors:
                st.table(top_factors)
            else:
                st.write("No top factors available")

            st.subheader("Explanations")
            explanations = result.get("explanations") or []
            if explanations:
                for item in explanations:
                    st.write("- ", item)
            else:
                st.write("No explanations available")

            st.subheader("Recommendations")
            recommendations = result.get("recommendations") or []
            if recommendations:
                for r in recommendations:
                    st.write("- ", r)
            else:
                st.write("No recommendations available")


def main():
    st.set_page_config(page_title="Single Customer Prediction")
    render_single_prediction()


if __name__ == "__main__":
    main()