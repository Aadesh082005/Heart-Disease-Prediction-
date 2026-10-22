
import streamlit as st

from src.models.predict import predict_heart_disease
from src.utils.config import MODEL_PATH
from src.utils.ui import (
    apply_custom_css,
    render_page_header,
    render_sidebar,
)

st.set_page_config(
    page_title="CardioAI | Prediction",
    page_icon="🫀",
    layout="wide",
)

apply_custom_css()
render_sidebar()

render_page_header(
    "Heart Prediction",
    "Enter dataset-compatible features to explore the model output.",
    "PREDICTION / ASSESSMENT",
)

st.info(
    "Educational demonstration only. This model is not a "
    "medical diagnostic tool."
)

if not MODEL_PATH.exists():
    st.warning(
        "The trained model is missing. Add a compatible dataset "
        "and run the training script first."
    )
    st.stop()

st.markdown("### Patient feature inputs")
st.caption("Use the coding and units documented by your dataset.")

with st.form("heart_prediction_form"):
    st.markdown("#### 01 · Basic information")
    c1, c2, c3 = st.columns(3)

    with c1:
        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=45,
        )
    with c2:
        sex = st.selectbox("Sex code", [0, 1])
    with c3:
        cp = st.selectbox("Chest pain type (cp)", [0, 1, 2, 3])

    st.divider()
    st.markdown("#### 02 · Measurements")
    c1, c2, c3 = st.columns(3)

    with c1:
        trestbps = st.number_input(
            "Resting blood pressure",
            min_value=50,
            max_value=300,
            value=120,
        )
    with c2:
        chol = st.number_input(
            "Cholesterol",
            min_value=50,
            max_value=700,
            value=200,
        )
    with c3:
        fbs = st.selectbox("Fasting blood sugar code", [0, 1])

    c1, c2, c3 = st.columns(3)

    with c1:
        restecg = st.selectbox("Resting ECG code", [0, 1, 2])
    with c2:
        thalach = st.number_input(
            "Maximum heart rate",
            min_value=40,
            max_value=250,
            value=150,
        )
    with c3:
        exang = st.selectbox(
            "Exercise-induced angina code",
            [0, 1],
        )

    st.divider()
    st.markdown("#### 03 · Additional features")
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        oldpeak = st.number_input(
            "Oldpeak",
            min_value=-5.0,
            max_value=10.0,
            value=0.0,
            step=0.1,
        )
    with c2:
        slope = st.selectbox("ST slope code", [0, 1, 2])
    with c3:
        ca = st.selectbox("CA code", [0, 1, 2, 3, 4])
    with c4:
        thal = st.selectbox("Thal code", [0, 1, 2, 3])

    st.write("")
    submitted = st.form_submit_button(
        "Run model prediction",
        type="primary",
        use_container_width=True,
    )

if submitted:
    input_data = {
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal,
    }

    try:
        result = predict_heart_disease(input_data)

        st.write("")
        st.markdown("### Model output")

        with st.container(border=True):
            if result["prediction"] == 1:
                st.warning(
                    "The model assigned the input to dataset class 1. "
                    "This is not a diagnosis."
                )
            else:
                st.info(
                    "The model assigned the input to dataset class 0. "
                    "This does not rule out heart disease."
                )

            st.metric(
                "Estimated probability of dataset class 1",
                f"{result['class_1_probability'] * 100:.1f}%",
            )

            st.caption(
                "This score is not necessarily calibrated clinical risk. "
                "Do not use it to make medical decisions."
            )

    except (ValueError, TypeError, FileNotFoundError) as exc:
        st.error(f"Prediction could not be generated: {exc}")
