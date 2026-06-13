import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))
    
import streamlit as st

from components.theme import apply_theme
apply_theme()

from pages.dashboard import render_dashboard
from pages.single_prediction import render_single_prediction
from pages.dataset_analysis import render_dataset_analysis
from pages.about import render_about


st.set_page_config(
    page_title="StayPulse",
    page_icon="📊",
    layout="wide"
)


def main():

    st.sidebar.title("📊 StayPulse")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Single Prediction",
            "Dataset Analysis",
            "About"
        ]
    )

    if page == "Dashboard":
        render_dashboard()

    elif page == "Single Prediction":
        render_single_prediction()

    elif page == "Dataset Analysis":
        render_dataset_analysis()

    elif page == "About":
        render_about()


if __name__ == "__main__":
    main()