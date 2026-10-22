
import json

import streamlit as st
import pandas as pd
import plotly.express as px

from src.utils.config import EVALUATION_PATH, METADATA_PATH
from src.utils.ui import (
    apply_custom_css,
    render_page_header,
    render_sidebar,
)

st.set_page_config(
    page_title="CardioAI | Performance",
    page_icon="📈",
    layout="wide",
)

apply_custom_css()
render_sidebar()

render_page_header(
    "Model Performance",
    "Review classification metrics from your model evaluation report.",
    "ANALYTICS / MODEL EVALUATION",
)

if not EVALUATION_PATH.exists():
    st.warning("Evaluation report not found. Train the model first.")
    st.stop()

try:
    metrics = json.loads(
        EVALUATION_PATH.read_text(encoding="utf-8")
    )

    if not metrics:
        st.warning("The evaluation report is empty.")
        st.stop()

    names = ["accuracy", "precision", "recall", "f1_score"]

    missing = [name for name in names if name not in metrics]
    if missing:
        st.error(f"Missing metrics: {', '.join(missing)}")
        st.stop()

    cols = st.columns(4)

    for col, key, label in zip(
        cols,
        names,
        ["Accuracy", "Precision", "Recall", "F1 Score"],
    ):
        value = float(metrics[key])
        if not 0 <= value <= 1:
            st.error(f"Invalid metric value for {key}.")
            st.stop()

        col.metric(label, f"{value * 100:.1f}%")

    st.write("")

    chart_data = pd.DataFrame(
        {
            "Metric": [
                "Accuracy",
                "Precision",
                "Recall",
                "F1 Score",
            ],
            "Score": [
                float(metrics["accuracy"]),
                float(metrics["precision"]),
                float(metrics["recall"]),
                float(metrics["f1_score"]),
            ],
        }
    )

    st.markdown("### Evaluation overview")

    fig = px.bar(
        chart_data,
        x="Metric",
        y="Score",
        text=chart_data["Score"].map(lambda x: f"{x:.2f}"),
        range_y=[0, 1],
        title="Classification metrics",
    )

    fig.update_traces(
        marker_color="#22D3EE",
        textposition="outside",
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#DCE7F5",
        yaxis_title="Score (0–1)",
        xaxis_title="",
    )

    st.plotly_chart(fig, use_container_width=True)

    if "roc_auc" in metrics:
        st.metric("ROC-AUC", f"{float(metrics['roc_auc']):.3f}")

    if "confusion_matrix" in metrics:
        st.markdown("### Confusion matrix")
        st.dataframe(
            pd.DataFrame(
                metrics["confusion_matrix"],
                index=["Actual class 0", "Actual class 1"],
                columns=["Predicted class 0", "Predicted class 1"],
            ),
            use_container_width=True,
        )

    if METADATA_PATH.exists():
        metadata = json.loads(
            METADATA_PATH.read_text(encoding="utf-8")
        )

        with st.expander("Model information"):
            st.write(
                "Model:",
                metadata.get("model_name", "Unknown"),
            )
            st.write(
                "Version:",
                metadata.get("model_version", "Unknown"),
            )
            st.write(
                "Features:",
                metadata.get("feature_names", []),
            )

    st.caption(
        "Metrics reflect the evaluation dataset only. They do not "
        "establish clinical validity or real-world medical accuracy."
    )

except (ValueError, OSError, TypeError) as exc:
    st.error(f"Unable to load the evaluation report: {exc}")
