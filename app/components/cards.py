"""
Cards Component - Reusable card components
"""

import streamlit as st
from .theme import COLORS, SPACING, RADIUS


def metric_card(
    title: str,
    value: str,
    subtitle: str = None,
    color: str = "primary",
    icon: str = None,
):
    """
    Display a metric card
    
    Args:
        title: Metric title
        value: Metric value to display
        subtitle: Optional subtitle/description
        color: Color name from theme
        icon: Optional emoji or icon
    """
    color_value = COLORS.get(color, COLORS["primary"])
    
    card_html = f"""
    <div style="
        background: linear-gradient(135deg, {COLORS['card_bg']} 0%, {COLORS['secondary_bg']} 100%);
        border: 1px solid {COLORS['border']};
        border-radius: {RADIUS['lg']};
        padding: {SPACING['lg']};
        margin-bottom: {SPACING['md']};
    ">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="flex: 1;">
                <div style="font-size: 12px; color: {COLORS['text_secondary']}; 
                            text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;">
                    {title}
                </div>
                <div style="font-size: 28px; font-weight: 700; color: {color_value}; margin-bottom: 4px;">
                    {value}
                </div>
                {f'<div style="font-size: 13px; color: {COLORS["text_secondary"]};">{subtitle}</div>' if subtitle else ''}
            </div>
            {f'<div style="font-size: 24px; margin-left: {SPACING["md"]};">{icon}</div>' if icon else ''}
        </div>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)


def risk_gauge_card(
    probability: float,
    risk_level: str,
):
    """
    Display a risk gauge card with probability
    
    Args:
        probability: Churn probability (0-100)
        risk_level: 'Low', 'Medium', or 'High'
    """
    # Determine color based on probability
    if probability >= 70:
        color = COLORS["danger"]
        color_name = "danger"
    elif probability >= 40:
        color = COLORS["warning"]
        color_name = "warning"
    else:
        color = COLORS["success"]
        color_name = "success"
    
    # Create gauge visualization
    gauge_percentage = probability
    gauge_html = f"""
    <div style="
        background: {COLORS['card_bg']};
        border: 1px solid {COLORS['border']};
        border-radius: {RADIUS['lg']};
        padding: {SPACING['lg']};
        margin-bottom: {SPACING['md']};
    ">
        <div style="text-align: center; margin-bottom: {SPACING['md']};">
            <div style="font-size: 12px; color: {COLORS['text_secondary']}; 
                        text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px;">
                Churn Probability
            </div>
            
            <div style="
                width: 100%;
                height: 12px;
                background: {COLORS['secondary_bg']};
                border-radius: {RADIUS['full']};
                overflow: hidden;
                margin-bottom: {SPACING['md']};
            ">
                <div style="
                    width: {gauge_percentage}%;
                    height: 100%;
                    background: linear-gradient(90deg, {COLORS['primary']} 0%, {color} 100%);
                    transition: width 0.3s ease;
                "></div>
            </div>
            
            <div style="font-size: 32px; font-weight: 700; color: {color}; margin-bottom: 4px;">
                {probability:.1f}%
            </div>
            <div style="font-size: 14px; color: {COLORS['text_secondary']};">
                Risk Level: <span style="color: {color}; font-weight: 600;">{risk_level}</span>
            </div>
        </div>
    </div>
    """
    
    st.markdown(gauge_html, unsafe_allow_html=True)


def status_card(
    status: str,
    title: str,
    description: str = None,
    color: str = "primary",
    icon: str = None,
):
    """
    Display a status card
    
    Args:
        status: Status text
        title: Card title
        description: Optional description
        color: Color name from theme
        icon: Optional emoji
    """
    color_value = COLORS.get(color, COLORS["primary"])
    
    card_html = f"""
    <div style="
        background: {COLORS['card_bg']};
        border: 1px solid {COLORS['border']};
        border-radius: {RADIUS['lg']};
        padding: {SPACING['lg']};
        margin-bottom: {SPACING['md']};
        border-left: 4px solid {color_value};
    ">
        <div style="display: flex; align-items: center; gap: {SPACING['md']}; margin-bottom: 8px;">
            {f'<span style="font-size: 20px;">{icon}</span>' if icon else ''}
            <span style="font-size: 12px; color: {color_value}; font-weight: 600; text-transform: uppercase;">
                {status}
            </span>
        </div>
        <div style="font-size: 16px; color: {COLORS['text_primary']}; font-weight: 600; margin-bottom: 4px;">
            {title}
        </div>
        {f'<div style="font-size: 14px; color: {COLORS["text_secondary"]};">{description}</div>' if description else ''}
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)


def insight_card(
    title: str,
    insights: list,
    icon: str = "💡",
):
    """
    Display an insights card with a list of insights
    
    Args:
        title: Card title
        insights: List of insight strings
        icon: Optional emoji
    """
    insights_html = "".join([
        f'<div style="margin-bottom: {SPACING["sm"]}; font-size: 14px; color: {COLORS["text_secondary"]};">'
        f'• {insight}</div>'
        for insight in insights
    ])
    
    card_html = f"""
    <div style="
        background: {COLORS['card_bg']};
        border: 1px solid {COLORS['border']};
        border-radius: {RADIUS['lg']};
        padding: {SPACING['lg']};
        margin-bottom: {SPACING['md']};
    ">
        <div style="display: flex; align-items: center; gap: {SPACING['md']}; margin-bottom: {SPACING['md']};">
            <span style="font-size: 20px;">{icon}</span>
            <span style="font-size: 14px; color: {COLORS['text_primary']}; font-weight: 600; text-transform: uppercase;">
                {title}
            </span>
        </div>
        <div style="margin-left: 28px;">
            {insights_html}
        </div>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)
