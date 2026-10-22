
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
CSS_FILE = ROOT / "assets" / "styles" / "custom.css"


def apply_custom_css():
    if CSS_FILE.exists():
        css = CSS_FILE.read_text(encoding="utf-8")
        st.markdown(
            f"<style>{css}</style>",
            unsafe_allow_html=True,
        )


def render_sidebar():
    with st.sidebar:
        st.markdown(
            """
            <div style="padding:8px 0 18px">
                <div style="font-size:34px">❤️</div>
                <div style="font-size:25px;font-weight:800">
                    Cardio<span style="color:#22d3ee">AI</span>
                </div>
                <div style="font-size:10px;letter-spacing:2px;
                            color:#93a4bb">
                    HEART HEALTH ANALYTICS
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.caption("YOUR WORKSPACE")
        st.page_link("app.py", label="Overview", icon="🏠")
        st.page_link(
            "pages/1_Heart_Prediction.py",
            label="Heart Prediction",
            icon="🫀",
        )
        st.page_link(
            "pages/2_Health_Insights.py",
            label="Health Insights",
            icon="📊",
        )
        st.page_link(
            "pages/3_Model_Performance.py",
            label="Model Performance",
            icon="📈",
        )
        st.page_link(
            "pages/4_About_Project.py",
            label="About Project",
            icon="ℹ️",
        )

        st.divider()
        st.caption("Educational ML application")
        st.caption("Not a medical diagnostic tool")


def render_page_header(title, subtitle, eyebrow="CARDIOAI WORKSPACE"):
    st.markdown(
        f"""
        <div class="eyebrow">{eyebrow}</div>
        <div style="font-size:32px;font-weight:800;
                    margin-top:8px;line-height:1.25">
            {title}
        </div>
        <div style="color:#93a4bb;margin-top:8px;
                    margin-bottom:22px">
            {subtitle}
        </div>
        """,
        unsafe_allow_html=True,
    )
