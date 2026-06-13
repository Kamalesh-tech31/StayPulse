"""
Metrics Component - KPI and metric calculations
"""

import pandas as pd
from utils.analytics import (
    analyze_churn_distribution,
    analyze_by_geography,
    analyze_by_age_group,
    calculate_revenue_at_risk,
)


def get_dashboard_metrics(df: pd.DataFrame) -> dict:
    """
    Calculate dashboard KPI metrics
    
    Args:
        df: DataFrame with customer data
    
    Returns:
        Dictionary with KPI metrics
    """
    # Determine churn column
    if "Churn_Probability" in df.columns:
        churn_col = "Churn_Probability"
        # Convert probability to binary for counting
        total_high_risk = len(df[df["Churn_Probability"] >= 70])
    elif "Predicted_Churn" in df.columns:
        churn_col = "Predicted_Churn"
        total_high_risk = df["Predicted_Churn"].sum()
    elif "Exited" in df.columns:
        churn_col = "Exited"
        total_high_risk = df["Exited"].sum()
    else:
        # Fallback
        return {
            "total_customers": len(df),
            "churn_rate": 0,
            "high_risk_customers": 0,
            "retention_rate": 100,
            "revenue_at_risk": 0,
        }
    
    churn_metrics = analyze_churn_distribution(df, churn_col)
    
    # Calculate revenue at risk
    revenue_at_risk = 0
    if "EstimatedSalary" in df.columns:
        if "Churn_Probability" in df.columns:
            # Use probability-weighted salary
            revenue_at_risk = calculate_revenue_at_risk(df)
        else:
            # Use actual churn predictions
            churned_indices = df[churn_col] == 1
            revenue_at_risk = df[churned_indices]["EstimatedSalary"].sum()
    
    return {
        "total_customers": churn_metrics["total_customers"],
        "churn_rate": churn_metrics["churn_rate"],
        "high_risk_customers": total_high_risk,
        "retention_rate": churn_metrics["retention_rate"],
        "revenue_at_risk": revenue_at_risk,
    }


def get_model_performance_metrics(accuracy: float, precision: float, 
                                   recall: float, f1_score: float) -> dict:
    """
    Package model performance metrics
    
    Args:
        accuracy: Model accuracy
        precision: Model precision
        recall: Model recall
        f1_score: Model F1 score
    
    Returns:
        Dictionary with metrics
    """
    return {
        "accuracy": round(accuracy * 100, 2),
        "precision": round(precision * 100, 2),
        "recall": round(recall * 100, 2),
        "f1_score": round(f1_score * 100, 2),
    }


def get_geographic_insights(df: pd.DataFrame) -> dict:
    """
    Get geographic analysis insights
    
    Args:
        df: DataFrame with Geography column
    
    Returns:
        Dictionary with geographic analysis
    """
    if "Churn_Probability" in df.columns:
        churn_col = "Churn_Probability"
    elif "Predicted_Churn" in df.columns:
        churn_col = "Predicted_Churn"
    elif "Exited" in df.columns:
        churn_col = "Exited"
    else:
        return {}
    
    geo_analysis = analyze_by_geography(df, churn_col)
    
    # Find highest risk geography
    if geo_analysis:
        highest_risk = max(
            geo_analysis.items(),
            key=lambda x: x[1]["churn_rate"]
        )
        
        return {
            "highest_risk_geography": highest_risk[0],
            "highest_risk_churn_rate": highest_risk[1]["churn_rate"],
            "all_geographies": geo_analysis,
        }
    
    return {}


def get_age_group_insights(df: pd.DataFrame) -> dict:
    """
    Get age group analysis insights
    
    Args:
        df: DataFrame with Age column
    
    Returns:
        Dictionary with age group analysis
    """
    if "Churn_Probability" in df.columns:
        churn_col = "Churn_Probability"
    elif "Predicted_Churn" in df.columns:
        churn_col = "Predicted_Churn"
    elif "Exited" in df.columns:
        churn_col = "Exited"
    else:
        return {}
    
    age_analysis = analyze_by_age_group(df, churn_col)
    
    # Find highest risk age group
    if age_analysis:
        highest_risk = max(
            age_analysis.items(),
            key=lambda x: x[1]["churn_rate"]
        )
        
        return {
            "highest_risk_age_group": highest_risk[0],
            "highest_risk_churn_rate": highest_risk[1]["churn_rate"],
            "all_age_groups": age_analysis,
        }
    
    return {}


def get_risk_summary(df: pd.DataFrame) -> dict:
    """
    Get overall risk summary
    
    Args:
        df: DataFrame with Risk_Level or predictions
    
    Returns:
        Dictionary with risk summary
    """
    summary = {}
    
    if "Risk_Level" in df.columns:
        risk_counts = df["Risk_Level"].value_counts().to_dict()
        total = len(df)
        
        summary = {
            "high_risk": risk_counts.get("High", 0),
            "medium_risk": risk_counts.get("Medium", 0),
            "low_risk": risk_counts.get("Low", 0),
            "high_risk_percentage": round((risk_counts.get("High", 0) / total * 100), 2) if total > 0 else 0,
            "medium_risk_percentage": round((risk_counts.get("Medium", 0) / total * 100), 2) if total > 0 else 0,
            "total_customers": total,
        }
    elif "Predicted_Churn" in df.columns:
        churned = (df["Predicted_Churn"] == 1).sum()
        total = len(df)
        
        summary = {
            "high_risk": churned,
            "low_risk": total - churned,
            "high_risk_percentage": round((churned / total * 100), 2) if total > 0 else 0,
            "total_customers": total,
        }
    
    return summary
