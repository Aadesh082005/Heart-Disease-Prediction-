import plotly.express as px
import pandas as pd


def create_target_chart(data):
    """Create a chart of target-class counts."""

    if "target" not in data.columns:
        raise ValueError(
            "Dataset must contain a target column."
        )

    counts = (
        data["target"]
        .value_counts()
        .sort_index()
        .rename_axis("Target")
        .reset_index(name="Count")
    )

    counts["Target"] = counts["Target"].map(
        {
            0: "Class 0",
            1: "Class 1",
        }
    ).fillna("Other")

    figure = px.bar(
        counts,
        x="Target",
        y="Count",
        title="Target Class Distribution",
        text="Count",
    )

    figure.update_layout(
        xaxis_title="Dataset Target Label",
        yaxis_title="Number of Records",
    )

    return figure


def create_age_distribution_chart(data):
    """Create an age-distribution histogram."""

    if "age" not in data.columns:
        raise ValueError(
            "Dataset must contain an age column."
        )

    figure = px.histogram(
        data,
        x="age",
        nbins=20,
        title="Age Distribution in Dataset",
    )

    figure.update_layout(
        xaxis_title="Age",
        yaxis_title="Number of Records",
    )

    return figure


def create_correlation_chart(data):
    """Create a correlation heatmap for numeric columns."""

    numeric_data = data.select_dtypes(
        include="number"
    )

    correlation = numeric_data.corr()

    figure = px.imshow(
        correlation,
        text_auto=".2f",
        aspect="auto",
        title="Feature Correlation Heatmap",
    )

    return figure