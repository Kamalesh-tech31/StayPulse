"""
Executive dashboard for churn predictions.

This page talks to the backend only through `ml_backend.predictor`:

from ml_backend.predictor import predict_dataset, get_model_feature_importance

It loads `dataset/Churn_Modelling.csv`, runs batch prediction, and displays
high-level metrics and charts.
"""

import streamlit as st
import pandas as pd

try:
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except Exception:
    PLOTLY_AVAILABLE = False

from ml_backend.predictor import predict_dataset, get_model_feature_importance

DATA_PATH = "dataset/Churn_Modelling.csv"

@st.cache_data(show_spinner=False)
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def safe_run_predictions(df: pd.DataFrame) -> pd.DataFrame:
    return predict_dataset(df)


def render_dashboard():
    st.title("Dashboard")
    st.subheader("Executive KPIs and Customer Risk Overview")
    st.markdown("---")

    st.markdown(
        "This dashboard loads the canonical dataset, runs batch predictions via the backend, and displays executive metrics."
    )

    try:
        df = load_data(DATA_PATH)
    except Exception as e:
        st.error(f"Failed to load dataset: {e}")
        return

    st.subheader("Dataset")
    st.write(f"Rows: {df.shape[0]} — Columns: {df.shape[1]}")
    st.dataframe(df.head())

    st.subheader("Run batch predictions")
    if st.button("Run predictions on dataset"):
        with st.spinner("Running batch predictions..."):
            try:
                predictions_df = safe_run_predictions(df)
            except Exception as e:
                st.error(f"Batch prediction failed: {e}")
                return

        # Validate expected columns
        expected = ["Predicted_Churn", "Churn_Probability", "Risk_Level"]
        missing = [c for c in expected if c not in predictions_df.columns]
        if missing:
            st.error(f"Prediction result missing expected columns: {missing}")
            return

        # Metrics
        total_customers = len(predictions_df)
        churn_rate = predictions_df["Predicted_Churn"].sum() / total_customers * 100 if total_customers else 0
        high_risk = int((predictions_df["Risk_Level"] == "High").sum())

        # Revenue at risk: sum(Balance * Churn_Probability/100)
        revenue_at_risk = 0.0
        if "Balance" in predictions_df.columns and "Churn_Probability" in predictions_df.columns:
            try:
                revenue_at_risk = (predictions_df["Balance"] * predictions_df["Churn_Probability"] / 100.0).sum()
            except Exception:
                revenue_at_risk = 0.0

        # Display top metrics in columns
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Customers", f"{total_customers}")
        c2.metric("Predicted Churn Rate", f"{churn_rate:.2f}%")
        c3.metric("High Risk Customers", f"{high_risk}")
        c4.metric("Revenue At Risk", f"${revenue_at_risk:,.2f}")

        # Risk distribution
        st.subheader("Risk Distribution")
        risk_counts = predictions_df["Risk_Level"].value_counts().rename_axis("Risk_Level").reset_index(name="count")

        if PLOTLY_AVAILABLE:
            fig = px.pie(risk_counts, names="Risk_Level", values="count", title="Risk Distribution")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.bar_chart(risk_counts.set_index("Risk_Level")["count"])

        # Top feature importance
        st.subheader("Top Feature Importance")
        try:
            features = get_model_feature_importance()
        except Exception as e:
            st.error(f"Failed to load feature importances: {e}")
            features = []

        if features:
            feat_df = pd.DataFrame(features)
            top10 = feat_df.head(10)
            st.table(top10)

            if PLOTLY_AVAILABLE:
                fig2 = px.bar(top10, x="feature", y="importance", title="Top 10 Features")
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.bar_chart(top10.set_index("feature")["importance"])
        else:
            st.write("No feature importance available")

        # Show full predictions table
        st.subheader("Predictions")
        st.dataframe(predictions_df)

    else:
        st.info("Click 'Run predictions on dataset' to generate the dashboard metrics.")


def main():
    st.set_page_config(page_title="Churn Dashboard", layout="wide")
    render_dashboard()


if __name__ == "__main__":
    main()
