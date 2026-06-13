"""
Charts Component - Data visualization using Plotly
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from .theme import COLORS


def get_plotly_template() -> dict:
    """Get custom Plotly template for premium styling"""
    return {
        "layout": go.Layout(
            template="plotly_dark",
            paper_bgcolor=COLORS["card_bg"],
            plot_bgcolor=COLORS["secondary_bg"],
            font=dict(
                family="Arial, sans-serif",
                size=12,
                color=COLORS["text_primary"],
            ),
            margin=dict(l=50, r=50, t=50, b=50),
            hovermode="closest",
            xaxis=dict(
                gridcolor=COLORS["border"],
                zeroline=False,
                showgrid=True,
                gridwidth=0.5,
            ),
            yaxis=dict(
                gridcolor=COLORS["border"],
                zeroline=False,
                showgrid=True,
                gridwidth=0.5,
            ),
        )
    }


def churn_distribution_chart(df: pd.DataFrame, churn_column: str = "Exited"):
    """
    Create churn distribution pie/donut chart
    
    Args:
        df: DataFrame with churn data
        churn_column: Name of churn column
    
    Returns:
        Plotly figure
    """
    if churn_column not in df.columns:
        return None
    
    churn_counts = df[churn_column].value_counts()
    labels = ["Retained", "Churned"]
    values = [churn_counts.get(0, 0), churn_counts.get(1, 0)]
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        marker=dict(
            colors=[COLORS["success"], COLORS["danger"]],
            line=dict(color=COLORS["card_bg"], width=2),
        ),
        textposition="inside",
        textinfo="label+percent",
        hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>",
    )])
    
    fig.update_layout(
        **get_plotly_template()["layout"],
        title=dict(
            text="Churn Distribution",
            font=dict(size=16, color=COLORS["text_primary"]),
        ),
        showlegend=False,
        height=350,
    )
    
    return fig


def geographic_distribution_chart(df: pd.DataFrame, churn_column: str = "Exited"):
    """
    Create geographic churn distribution
    
    Args:
        df: DataFrame with Geography column
        churn_column: Name of churn column
    
    Returns:
        Plotly figure
    """
    if "Geography" not in df.columns:
        return None
    
    geo_churn = df.groupby("Geography")[churn_column].agg(["sum", "count"])
    geo_churn["churn_rate"] = (geo_churn["sum"] / geo_churn["count"] * 100).round(1)
    geo_churn = geo_churn.reset_index()
    
    fig = go.Figure(data=[
        go.Bar(
            x=geo_churn["Geography"],
            y=geo_churn["churn_rate"],
            marker=dict(
                color=geo_churn["churn_rate"],
                colorscale=[[0, COLORS["success"]], [1, COLORS["danger"]]],
                showscale=False,
            ),
            text=geo_churn["churn_rate"].apply(lambda x: f"{x:.1f}%"),
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>Churn Rate: %{y:.1f}%<extra></extra>",
        )
    ])
    
    fig.update_layout(
        **get_plotly_template()["layout"],
        title=dict(
            text="Churn Rate by Geography",
            font=dict(size=16, color=COLORS["text_primary"]),
        ),
        xaxis_title="Geography",
        yaxis_title="Churn Rate (%)",
        height=350,
        showlegend=False,
    )
    
    return fig


def age_distribution_chart(df: pd.DataFrame):
    """
    Create age distribution histogram
    
    Args:
        df: DataFrame with Age column
    
    Returns:
        Plotly figure
    """
    if "Age" not in df.columns:
        return None
    
    fig = go.Figure(data=[
        go.Histogram(
            x=df["Age"],
            nbinsx=20,
            marker=dict(
                color=COLORS["primary"],
                line=dict(color=COLORS["primary_dark"], width=1),
            ),
            hovertemplate="<b>Age Range</b><br>Count: %{y}<extra></extra>",
        )
    ])
    
    fig.update_layout(
        **get_plotly_template()["layout"],
        title=dict(
            text="Customer Age Distribution",
            font=dict(size=16, color=COLORS["text_primary"]),
        ),
        xaxis_title="Age (years)",
        yaxis_title="Number of Customers",
        height=350,
        showlegend=False,
    )
    
    return fig


def balance_distribution_chart(df: pd.DataFrame):
    """
    Create balance distribution histogram
    
    Args:
        df: DataFrame with Balance column
    
    Returns:
        Plotly figure
    """
    if "Balance" not in df.columns:
        return None
    
    fig = go.Figure(data=[
        go.Histogram(
            x=df["Balance"],
            nbinsx=30,
            marker=dict(
                color=COLORS["primary_light"],
                line=dict(color=COLORS["primary"], width=1),
            ),
            hovertemplate="<b>Balance Range</b><br>Count: %{y}<extra></extra>",
        )
    ])
    
    fig.update_layout(
        **get_plotly_template()["layout"],
        title=dict(
            text="Account Balance Distribution",
            font=dict(size=16, color=COLORS["text_primary"]),
        ),
        xaxis_title="Balance ($)",
        yaxis_title="Number of Accounts",
        height=350,
        showlegend=False,
    )
    
    return fig


def salary_distribution_chart(df: pd.DataFrame):
    """
    Create salary distribution histogram
    
    Args:
        df: DataFrame with EstimatedSalary column
    
    Returns:
        Plotly figure
    """
    if "EstimatedSalary" not in df.columns:
        return None
    
    fig = go.Figure(data=[
        go.Histogram(
            x=df["EstimatedSalary"],
            nbinsx=30,
            marker=dict(
                color=COLORS["primary_light"],
                line=dict(color=COLORS["primary"], width=1),
            ),
            hovertemplate="<b>Salary Range</b><br>Count: %{y}<extra></extra>",
        )
    ])
    
    fig.update_layout(
        **get_plotly_template()["layout"],
        title=dict(
            text="Estimated Salary Distribution",
            font=dict(size=16, color=COLORS["text_primary"]),
        ),
        xaxis_title="Salary ($)",
        yaxis_title="Number of Customers",
        height=350,
        showlegend=False,
    )
    
    return fig


def feature_importance_chart(importance_dict: dict, top_n: int = 10):
    """
    Create feature importance bar chart
    
    Args:
        importance_dict: Dictionary with feature importance scores
        top_n: Number of top features to show
    
    Returns:
        Plotly figure
    """
    if not importance_dict:
        return None
    
    # Get top N features
    top_features = dict(list(importance_dict.items())[:top_n])
    features = list(top_features.keys())
    importances = list(top_features.values())
    
    fig = go.Figure(data=[
        go.Bar(
            y=features,
            x=importances,
            orientation="h",
            marker=dict(
                color=importances,
                colorscale=[[0, COLORS["primary_light"]], [1, COLORS["primary_dark"]]],
                showscale=False,
            ),
            text=importances,
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>Importance: %{x:.2f}<extra></extra>",
        )
    ])
    
    fig.update_layout(
        **get_plotly_template()["layout"],
        title=dict(
            text="Top Features by Importance",
            font=dict(size=16, color=COLORS["text_primary"]),
        ),
        xaxis_title="Importance Score",
        height=400,
        showlegend=False,
        yaxis=dict(autorange="reversed"),
    )
    
    return fig


def confusion_matrix_heatmap(cm: np.ndarray):
    """
    Create confusion matrix heatmap
    
    Args:
        cm: Confusion matrix array
    
    Returns:
        Plotly figure
    """
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=["Not Churned", "Churned"],
        y=["Not Churned", "Churned"],
        colorscale=[[0, COLORS["success"]], [1, COLORS["danger"]]],
        text=cm,
        texttemplate="%{text}",
        textfont={"size": 14},
        colorbar=dict(
            title="Count",
            titleside="right",
        ),
        hovertemplate="<b>%{y}</b> → <b>%{x}</b><br>Count: %{z}<extra></extra>",
    ))
    
    fig.update_layout(
        **get_plotly_template()["layout"],
        title=dict(
            text="Confusion Matrix",
            font=dict(size=16, color=COLORS["text_primary"]),
        ),
        xaxis_title="Predicted",
        yaxis_title="Actual",
        height=400,
    )
    
    return fig


def roc_curve_chart(fpr: np.ndarray, tpr: np.ndarray, auc: float):
    """
    Create ROC curve
    
    Args:
        fpr: False positive rate
        tpr: True positive rate
        auc: Area under curve
    
    Returns:
        Plotly figure
    """
    fig = go.Figure()
    
    # ROC Curve
    fig.add_trace(go.Scatter(
        x=fpr,
        y=tpr,
        mode="lines",
        name=f"ROC Curve (AUC = {auc:.3f})",
        line=dict(color=COLORS["primary"], width=3),
        hovertemplate="<b>FPR:</b> %{x:.3f}<br><b>TPR:</b> %{y:.3f}<extra></extra>",
    ))
    
    # Diagonal line
    fig.add_trace(go.Scatter(
        x=[0, 1],
        y=[0, 1],
        mode="lines",
        name="Random Classifier",
        line=dict(color=COLORS["text_secondary"], width=2, dash="dash"),
        hoverinfo="skip",
    ))
    
    fig.update_layout(
        **get_plotly_template()["layout"],
        title=dict(
            text="ROC Curve",
            font=dict(size=16, color=COLORS["text_primary"]),
        ),
        xaxis_title="False Positive Rate",
        yaxis_title="True Positive Rate",
        height=400,
    )
    
    return fig


def risk_distribution_chart(df: pd.DataFrame):
    """
    Create risk level distribution pie chart
    
    Args:
        df: DataFrame with Risk_Level column
    
    Returns:
        Plotly figure
    """
    if "Risk_Level" not in df.columns:
        return None
    
    risk_counts = df["Risk_Level"].value_counts()
    
    fig = go.Figure(data=[go.Pie(
        labels=risk_counts.index,
        values=risk_counts.values,
        marker=dict(
            colors=[
                COLORS["success"] if x == "Low" 
                else COLORS["warning"] if x == "Medium"
                else COLORS["danger"]
                for x in risk_counts.index
            ],
            line=dict(color=COLORS["card_bg"], width=2),
        ),
        textposition="inside",
        textinfo="label+percent",
        hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>",
    )])
    
    fig.update_layout(
        **get_plotly_template()["layout"],
        title=dict(
            text="Risk Level Distribution",
            font=dict(size=16, color=COLORS["text_primary"]),
        ),
        height=350,
    )
    
    return fig
