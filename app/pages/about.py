import streamlit as st


def render_about():

    st.title("About StayPulse")

    st.markdown("""
    ## Customer Churn Prediction Platform

    StayPulse is an AI-powered customer retention analytics platform.

    ### Features

    - Customer churn prediction
    - Risk classification
    - Explainable AI insights
    - Batch dataset analysis
    - Retention recommendations

    ### Machine Learning

    Models Used:

    - Random Forest Classifier
    - Logistic Regression

    ### Dataset

    Bank Customer Churn Dataset

    ### Developed Using

    - Python
    - Streamlit
    - Scikit-Learn
    - Pandas
    - Plotly
    """)