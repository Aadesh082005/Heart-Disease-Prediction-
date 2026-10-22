
import streamlit as st

from src.utils.ui import (
    apply_custom_css,
    render_page_header,
    render_sidebar,
)

st.set_page_config(
    page_title="CardioAI | About",
    page_icon="ℹ️",
    layout="wide",
)

apply_custom_css()
render_sidebar()

render_page_header(
    "About CardioAI",
    "Project overview, technology stack and responsible-use information.",
    "PROJECT / DOCUMENTATION",
)

st.markdown(
    """
    <div style="
        padding:28px;
        border:1px solid rgba(34,211,238,.22);
        border-radius:20px;
        background:linear-gradient(120deg,#132943,#111b2e);
    ">
        <div style="font-size:38px">❤️</div>
        <div style="font-size:30px;font-weight:800;margin:8px 0">
            Cardio<span style="color:#22d3ee">AI</span>
        </div>
        <div style="color:#93a4bb">
            HEART DISEASE CLASSIFICATION · MACHINE LEARNING PROJECT
        </div>
        <p style="margin-top:18px;line-height:1.8">
            An educational application demonstrating how structured
            data can be processed by a machine learning classifier
            and presented through an interactive dashboard.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

left, right = st.columns(2)

with left:
    with st.container(border=True):
        st.markdown("### 🧠 Technology stack")
        st.markdown(
            """
            - Python
            - Pandas and NumPy
            - Scikit-learn
            - Random Forest
            - Streamlit
            - Plotly
            - Joblib
            """
        )

    with st.container(border=True):
        st.markdown("### ⚙️ Project workflow")
        st.markdown(
            """
            1. Dataset validation
            2. Data preprocessing
            3. Train/test split
            4. Model training
            5. Evaluation
            6. Interactive model output
            """
        )

with right:
    with st.container(border=True):
        st.markdown("### 🎯 Project objectives")
        st.markdown(
            """
            - Demonstrate a classification pipeline
            - Explore dataset distributions
            - Display evaluation metrics
            - Practice Python and ML development
            """
        )

    with st.container(border=True):
        st.markdown("### 🚀 Future improvements")
        st.markdown(
            """
            - External validation
            - Better model calibration
            - Improved accessibility
            - Reproducible experiment tracking
            - Automated testing
            """
        )

st.error(
    "**Responsible use:** CardioAI is not a clinically validated "
    "medical tool. Its output must not be used to diagnose or rule "
    "out disease, choose treatment, or delay medical care."
)
