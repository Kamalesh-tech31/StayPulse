import streamlit as st


def render_home():
    st.title("StayPulse")
    st.subheader("AI-Powered Customer Churn Intelligence")
    st.markdown(
        "Predict customer churn before it happens, identify high-risk customers, and make data-driven retention decisions."
    )
    st.markdown("---")

    st.subheader("Quick Overview")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Customer Churn Prediction")
            st.markdown("Analyze a customer and receive an instant churn assessment.")
            st.markdown("### Batch Dataset Analysis")
            st.markdown("Perform large-scale churn prediction on customer datasets.")
        with col2:
            st.markdown("### Explainable AI Insights")
            st.markdown("See the drivers behind each prediction with transparent explanations.")
            st.markdown("### Retention Recommendations")
            st.markdown("Get actionable guidance for reducing churn and improving loyalty.")
    st.markdown("---")

    st.subheader("Business Impact")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Reduce Customer Churn")
            st.markdown("Detect at-risk customers before they leave.")
            st.markdown("### Protect Revenue")
            st.markdown("Identify revenue at risk and act before losses grow.")
        with col2:
            st.markdown("### Improve Retention Campaigns")
            st.markdown("Focus resources on customers who need it most.")
            st.markdown("### Data-Driven Decisions")
            st.markdown("Use predictive insights to guide retention strategy.")
    st.markdown("---")

    st.subheader("Get Started")
    st.markdown("Use the sidebar to open:")
    st.markdown("- Dashboard")
    st.markdown("- Single Prediction")
    st.markdown("- Dataset Analysis")
