import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))
    
import streamlit as st

from pages.dashboard import render_dashboard
from pages.single_prediction import render_single_prediction
from pages.dataset_analysis import render_dataset_analysis
from pages.about import render_about
from pages.home import render_home


st.set_page_config(
    page_title="StayPulse",
    page_icon="💠",
    layout="wide"
)

st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():

    st.sidebar.title("💠 StayPulse")

    st.sidebar.caption("AI Customer Retention Platform")
    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "",
        [
            "Home",
            "Dashboard",
            "Single Prediction",
            "Dataset Analysis",
            "About"
        ],
        label_visibility="collapsed"
    )

    if page == "Home":
        render_home()

    elif page == "Dashboard":
        render_dashboard()

    elif page == "Single Prediction":
        render_single_prediction()

    elif page == "Dataset Analysis":
        render_dataset_analysis()

    elif page == "About":
        render_about()


if __name__ == "__main__":
    main()