
import streamlit as st

from src.utils.config import DATASET_PATH, MODEL_PATH
from src.utils.ui import (
    apply_custom_css,
    render_page_header,
    render_sidebar,
)

st.set_page_config(
    page_title="CardioAI | Overview",
    page_icon="❤️",
    layout="wide",
)

apply_custom_css()
render_sidebar()


def main():
    render_page_header(
        "Heart Health Dashboard",
        "Your central workspace for machine learning and dataset insights.",
        "OVERVIEW / DASHBOARD",
    )

    st.markdown(
        """
        <div style="
            padding:32px;
            border-radius:22px;
            border:1px solid rgba(34,211,238,.24);
            background:linear-gradient(120deg,#132943,#101a2d 65%,#271b32);
        ">
            <div class="eyebrow">INTELLIGENCE MEETS HEALTH DATA</div>
            <div style="font-size:clamp(27px,4vw,42px);
                        font-weight:850;line-height:1.2;
                        margin:14px 0;color:#edf4ff">
                Explore your data.<br>
                Understand your model.
            </div>
            <div style="max-width:650px;color:#b4c4d9;
                        font-size:15px;line-height:1.8">
                An interactive machine learning demonstration for
                exploring heart disease dataset patterns and
                classification outputs.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Dataset",
            "Available" if DATASET_PATH.exists() else "Missing",
        )
        st.caption("Source data status")

    with col2:
        st.metric(
            "ML Model",
            "Ready" if MODEL_PATH.exists() else "Not trained",
        )
        st.caption("Trained model status")

    with col3:
        st.metric("Workspace", "Active")
        st.caption("Application interface")

    st.write("")
    st.subheader("Explore your workspace")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### 🫀 Heart Prediction")
            st.write("Enter model features and inspect the output.")
            st.page_link(
                "pages/1_Heart_Prediction.py",
                label="Open prediction",
                icon="🩺",
                use_container_width=True,
            )

        with st.container(border=True):
            st.markdown("### 📊 Health Insights")
            st.write("Explore distributions and feature correlations.")
            st.page_link(
                "pages/2_Health_Insights.py",
                label="Explore insights",
                icon="📊",
                use_container_width=True,
            )

    with col2:
        with st.container(border=True):
            st.markdown("### 📈 Model Performance")
            st.write("Review the evaluation report and metrics.")
            st.page_link(
                "pages/3_Model_Performance.py",
                label="View performance",
                icon="📈",
                use_container_width=True,
            )

        with st.container(border=True):
            st.markdown("### ℹ️ About CardioAI")
            st.write("Learn about the model, workflow and limitations.")
            st.page_link(
                "pages/4_About_Project.py",
                label="About this project",
                icon="ℹ️",
                use_container_width=True,
            )

    st.write("")
    st.warning(
        "Medical disclaimer: This is an educational application, "
        "not a clinically validated diagnostic tool. Its output "
        "cannot diagnose or rule out heart disease or guide treatment."
    )

    st.caption("CardioAI • Machine Learning Project")


if __name__ == "__main__":
    main()
