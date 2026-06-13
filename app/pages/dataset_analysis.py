import io

import streamlit as st
import pandas as pd

from ml_backend.predictor import predict_dataset


st.set_page_config(page_title="Dataset Analysis")

st.title("Batch Customer Prediction — Dataset Analysis")

st.markdown("Upload a CSV of customer records (columns should match the single prediction fields) and run batch prediction.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Failed to read CSV: {e}")
        st.stop()

    st.subheader("Dataset Overview")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    st.subheader("Preview")
    st.dataframe(df.head())

    if st.button("Run Batch Prediction"):
        st.info("Running predictions — this may take a moment...")
        try:
            result_df = predict_dataset(df)
        except Exception as e:
            st.error(f"Batch prediction failed: {e}")
        else:
            expected_cols = ["Predicted_Churn", "Churn_Probability", "Risk_Level"]
            missing = [c for c in expected_cols if c not in result_df.columns]
            if missing:
                st.error(f"Prediction result missing expected columns: {missing}")
            else:
                st.success("Predictions completed")

                st.subheader("Prediction Summary")
                total = len(result_df)
                high = int((result_df["Risk_Level"] == "High").sum())
                medium = int((result_df["Risk_Level"] == "Medium").sum())
                low = int((result_df["Risk_Level"] == "Low").sum())

                st.write("Total Customers:", total)
                st.write("High Risk Customers:", high)
                st.write("Medium Risk Customers:", medium)
                st.write("Low Risk Customers:", low)

                st.subheader("Predictions")
                st.dataframe(result_df)

                csv_bytes = result_df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="Download predictions as CSV",
                    data=csv_bytes,
                    file_name="predictions.csv",
                    mime="text/csv"
                )
else:
    st.info("Upload a CSV file to enable batch prediction.")