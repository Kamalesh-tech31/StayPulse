"""
Branding Components - Consistent StayPulse branding across app
"""

import streamlit as st
from .theme import COLORS, SPACING, TYPOGRAPHY


def render_app_header(title: str = "StayPulse", subtitle: str = "Customer Retention Intelligence Platform", icon: str = "📊"):
    """
    Render premium app header with branding
    
    Args:
        title: Main title (default: StayPulse)
        subtitle: Subtitle/description
        icon: Icon emoji
    """
    col1, col2 = st.columns([0.8, 4])
    
    with col1:
        st.markdown(
            f"""
            <div style="font-size: 28px; margin-top: 8px;">
                {icon}
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            f"""
            <div style="margin-top: 2px;">
                <h1 style="
                    margin: 0;
                    font-size: 28px;
                    font-weight: 700;
                    color: {COLORS['text_primary']};
                ">
                    {title}
                </h1>
                <p style="
                    margin: 4px 0 0 0;
                    font-size: 13px;
                    color: {COLORS['text_secondary']};
                    font-weight: 500;
                    letter-spacing: 0.3px;
                ">
                    {subtitle}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("---")


def render_sidebar_branding():
    """
    Render sidebar branding section with title and subtitle
    """
    st.markdown(
        f"""
        <div style="
            padding: {SPACING['md']};
            border-bottom: 1px solid {COLORS['border']};
            margin-bottom: {SPACING['lg']};
        ">
            <div style="
                font-size: 24px;
                font-weight: 700;
                margin-bottom: 4px;
                display: flex;
                align-items: center;
                gap: 8px;
            ">
                📊 <span>StayPulse</span>
            </div>
            <div style="
                font-size: 11px;
                color: {COLORS['text_secondary']};
                font-weight: 500;
                letter-spacing: 0.2px;
                line-height: 1.3;
            ">
                Customer Retention<br>Intelligence Platform
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_page_header(title: str, icon: str = "", description: str = ""):
    """
    Render standard page header with optional icon and description
    
    Args:
        title: Page title
        icon: Optional icon emoji
        description: Optional description/subtitle
    """
    header_text = f"{icon} {title}" if icon else title
    
    st.markdown(
        f"""
        <h2 style="
            margin: 0 0 {SPACING['sm']} 0;
            font-size: 24px;
            font-weight: 700;
            color: {COLORS['text_primary']};
        ">
            {header_text}
        </h2>
        """,
        unsafe_allow_html=True
    )
    
    if description:
        st.markdown(
            f"""
            <p style="
                margin: 0 0 {SPACING['md']} 0;
                font-size: 13px;
                color: {COLORS['text_secondary']};
            ">
                {description}
            </p>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("---")


def render_section_divider():
    """Render section divider"""
    st.markdown("---")


def render_section_header(title: str, subtitle: str = ""):
    """
    Render section header within a page
    
    Args:
        title: Section title
        subtitle: Optional subtitle
    """
    st.markdown(
        f"""
        <div style="margin: {SPACING['lg']} 0 {SPACING['md']} 0;">
            <h3 style="
                margin: 0 0 4px 0;
                font-size: 18px;
                font-weight: 600;
                color: {COLORS['text_primary']};
            ">
                {title}
            </h3>
            {f'<p style="margin: 0; font-size: 12px; color: {COLORS["text_secondary"]};">{subtitle}</p>' if subtitle else ''}
        </div>
        """,
        unsafe_allow_html=True
    )
