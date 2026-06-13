"""
Sidebar Component - Navigation and page selection
"""

import streamlit as st
from .theme import COLORS, SPACING, RADIUS
from .branding import render_sidebar_branding


def render_sidebar() -> str:
    """
    Render premium sidebar navigation
    
    Returns:
        Selected page name
    """
    # Render branding section with title and subtitle
    st.sidebar.markdown("")
    render_sidebar_branding()
    st.sidebar.markdown("")
    
    # Navigation items
    pages = {
        "Dashboard": "📈",
        "Dataset Analysis": "📑",
        "Single Prediction": "🎯",
        "About": "ℹ️",
    }
    
    # Get current page from session state
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Dashboard"
    
    st.sidebar.markdown("### Navigation")
    
    for page_name, icon in pages.items():
        is_active = st.session_state.current_page == page_name
        
        # Create button-like element
        button_html = f"""
        <div style="
            margin-bottom: {SPACING['md']};
        ">
            <button onclick="document.body.click()" style="
                width: 100%;
                text-align: left;
                padding: {SPACING['md']};
                border-radius: {RADIUS['md']};
                border: 1px solid {COLORS['primary'] if is_active else COLORS['border']};
                background-color: {'rgba(220, 38, 38, 0.1)' if is_active else 'transparent'};
                color: {COLORS['primary'] if is_active else COLORS['text_secondary']};
                font-weight: {'600' if is_active else '400'};
                cursor: pointer;
                transition: all 0.2s ease;
                display: flex;
                align-items: center;
                gap: {SPACING['md']};
                font-size: 14px;
            " class="nav-button" onmouseover="this.style.borderColor='{COLORS['primary']}'" 
               onmouseout="this.style.borderColor={COLORS['primary'] if is_active else COLORS['border']}">
                <span style="font-size: 18px;">{icon}</span>
                <span>{page_name}</span>
            </button>
        </div>
        """
        
        if st.sidebar.button(f"{icon} {page_name}", key=f"nav_{page_name}"):
            st.session_state.current_page = page_name
            st.rerun()
    
    st.sidebar.divider()
    
    # Additional info
    st.sidebar.markdown("### About StayPulse")
    st.sidebar.markdown(
        """
        Premium customer churn prediction platform 
        for financial institutions.
        
        **Version:** 1.0.0
        """
    )
    
    return st.session_state.current_page


def get_page_title(page_name: str) -> tuple:
    """
    Get page title and icon
    
    Args:
        page_name: Name of the page
    
    Returns:
        Tuple of (title, icon, subtitle)
    """
    page_info = {
        "Dashboard": (
            "Dashboard",
            "📈",
            "Executive overview of churn analytics"
        ),
        "Dataset Analysis": (
            "Dataset Analysis",
            "📑",
            "Analyze uploaded customer datasets"
        ),
        "Single Prediction": (
            "Single Customer Prediction",
            "🎯",
            "Predict churn for individual customers"
        ),
        "About": (
            "About StayPulse",
            "ℹ️",
            "Project overview and information"
        ),
    }
    
    return page_info.get(page_name, ("Unknown", "❓", ""))


def render_page_header(page_name: str):
    """
    Render page header with title
    
    Args:
        page_name: Name of current page
    """
    title, icon, subtitle = get_page_title(page_name)
    
    header_html = f"""
    <div style="
        padding: {SPACING['lg']} {SPACING['xl']};
        background: linear-gradient(135deg, {COLORS['secondary_bg']} 0%, {COLORS['card_bg']} 100%);
        border-bottom: 1px solid {COLORS['border']};
        margin: -64px -42px 0 -42px;
        margin-bottom: {SPACING['xl']};
        padding-top: {SPACING['2xl']};
    ">
        <div style="display: flex; align-items: center; gap: {SPACING['lg']}; margin-bottom: 8px;">
            <span style="font-size: 32px;">{icon}</span>
            <h1 style="
                font-size: 28px;
                font-weight: 700;
                color: {COLORS['text_primary']};
                margin: 0;
            ">{title}</h1>
        </div>
        <p style="
            color: {COLORS['text_secondary']};
            font-size: 14px;
            margin: 0;
        ">{subtitle}</p>
    </div>
    """
    
    st.markdown(header_html, unsafe_allow_html=True)
