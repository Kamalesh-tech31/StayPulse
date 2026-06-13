"""
Premium SaaS Theme Configuration
Inspired by Stripe, Linear, and Apple design systems
"""

import streamlit as st

# Color Palette
COLORS = {
    "background": "#0D0D0D",
    "secondary_bg": "#1a1a1a",
    "card_bg": "#1e1e1e",
    "primary": "#DC2626",
    "primary_dark": "#b81c1c",
    "primary_light": "#ef5350",
    "text_primary": "#FFFFFF",
    "text_secondary": "#b3b3b3",
    "text_tertiary": "#808080",
    "success": "#dc2626",
    "warning": "#ef4444",
    "danger": "#ef4444",
    "border": "#2a2a2a",
}

# Spacing Scale
SPACING = {
    "xs": "4px",
    "sm": "8px",
    "md": "16px",
    "lg": "24px",
    "xl": "32px",
    "2xl": "48px",
}

# Border Radius
RADIUS = {
    "sm": "8px",
    "md": "12px",
    "lg": "16px",
    "full": "9999px",
}

# Typography
TYPOGRAPHY = {
    "h1": {"size": "32px", "weight": 700},
    "h2": {"size": "28px", "weight": 700},
    "h3": {"size": "24px", "weight": 600},
    "body": {"size": "16px", "weight": 400},
    "body_sm": {"size": "14px", "weight": 400},
    "label": {"size": "12px", "weight": 600},
}


def apply_theme():
    """Apply premium SaaS theme to Streamlit app"""
    st.set_page_config(
        page_title="StayPulse",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Custom CSS for premium styling
    st.markdown(
        f"""
        <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        [data-testid="stMainBlockContainer"] {{
            background-color: {COLORS['background']};
            color: {COLORS['text_primary']};
        }}

        [data-testid="stAppViewContainer"] {{
            background-color: {COLORS['background']};
        }}

        /* Sidebar Styling */
        [data-testid="stSidebar"] {{
            background-color: {COLORS['secondary_bg']};
            border-right: 1px solid {COLORS['border']};
        }}

        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {{
            color: {COLORS['text_primary']};
        }}

        /* Cards */
        .stCard {{
            background-color: {COLORS['card_bg']};
            border: 1px solid {COLORS['border']};
            border-radius: {RADIUS['lg']};
            padding: {SPACING['lg']};
        }}

        /* Buttons */
        .stButton > button {{
            background-color: {COLORS['primary']};
            color: {COLORS['text_primary']};
            border: none;
            border-radius: {RADIUS['lg']};
            padding: 10px 20px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }}

        .stButton > button:hover {{
            background-color: {COLORS['primary_dark']};
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(220, 38, 38, 0.4);
        }}

        /* Input Fields */
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input,
        .stSelectbox > div > div > select {{
            background-color: {COLORS['card_bg']};
            border: 1px solid {COLORS['border']};
            border-radius: {RADIUS['md']};
            color: {COLORS['text_primary']};
            padding: 10px 12px;
        }}

        .stTextInput > div > div > input:focus,
        .stNumberInput > div > div > input:focus,
        .stSelectbox > div > div > select:focus {{
            border-color: {COLORS['primary']};
            box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
        }}

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 0;
            border-bottom: 1px solid {COLORS['border']};
        }}

        .stTabs [data-baseweb="tab"] {{
            background-color: transparent;
            color: {COLORS['text_secondary']};
            border-radius: 0;
            padding: 16px 24px;
            border-bottom: 2px solid transparent;
        }}

        .stTabs [aria-selected="true"] {{
            color: {COLORS['primary']};
            border-bottom: 2px solid {COLORS['primary']};
        }}

        /* Sidebar Styling */
        [data-testid="stSidebar"] {{
            background-color: {COLORS['secondary_bg']};
            border-right: 1px solid {COLORS['border']};
        }}

        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {{
            color: {COLORS['text_primary']};
        }}

        /* Metrics */
        .metric-container {{
            background-color: {COLORS['card_bg']};
            border: 1px solid {COLORS['border']};
            border-radius: {RADIUS['lg']};
            padding: {SPACING['lg']};
        }}

        /* Progress Bar */
        .stProgress > div > div > div > div {{
            background-color: {COLORS['primary']};
        }}

        /* Spinners and Loading */
        .stSpinner > div > div {{
            border-color: {COLORS['primary']};
            border-right-color: transparent;
        }}

        /* Text Colors */
        .text-primary {{
            color: {COLORS['text_primary']};
        }}

        .text-secondary {{
            color: {COLORS['text_secondary']};
        }}

        .text-tertiary {{
            color: {COLORS['text_tertiary']};
        }}

        /* Success/Warning/Danger */
        .text-success {{
            color: {COLORS['success']};
        }}

        .text-warning {{
            color: {COLORS['warning']};
        }}

        .text-danger {{
            color: {COLORS['danger']};
        }}

        /* Scrollbar Styling */
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}

        ::-webkit-scrollbar-track {{
            background: {COLORS['card_bg']};
        }}

        ::-webkit-scrollbar-thumb {{
            background: {COLORS['border']};
            border-radius: 4px;
        }}

        ::-webkit-scrollbar-thumb:hover {{
            background: {COLORS['text_tertiary']};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_color(name: str) -> str:
    """Get color from palette"""
    return COLORS.get(name, COLORS["text_primary"])


def get_spacing(size: str) -> str:
    """Get spacing value"""
    return SPACING.get(size, SPACING["md"])


def get_radius(size: str) -> str:
    """Get border radius value"""
    return RADIUS.get(size, RADIUS["md"])
