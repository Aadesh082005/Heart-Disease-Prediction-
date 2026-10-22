
import streamlit as st

from src.data.preprocessing import clean_dataset, load_dataset
from src.utils.config import DATASET_PATH
from src.utils.ui import (
    apply_custom_css,
    render_page_header,
    render_sidebar,
)
from src.visualization.charts import (
    create_age_distribution_chart,
    create_correlation_chart,
    create_target_chart,
)

st.set_page_config(
    page_title="CardioAI | Insights",
    page_icon="📊",
    layout="wide",
)

apply_custom_css()
render_sidebar()

render_page_header(
    "Health Insights",
    "Explore the structure, distributions and relationships in your dataset.",
    "ANALYTICS / DATA EXPLORATION",
)

if not DATASET_PATH.exists():
    st.warning("Dataset not found at data/raw/heart.csv.")
    st.stop()

try:
    data = clean_dataset(load_dataset(DATASET_PATH))

    c1, c2, c3 = st.columns(3)

    c1.metric("Dataset records", f"{len(data):,}")
    c2.metric("Features", len(data.columns) - 1)
    c3.metric("Missing values", int(data.isna().sum().sum()))

    st.write("")

    tab1, tab2, tab3 = st.tabs(
        ["Target distribution", "Age distribution", "Correlations"]
    )

    with tab1:
        st.markdown("### Target class distribution")
        st.caption(
            "Counts of the dataset's target labels; labels depend "
            "on the source dataset."
        )
        st.plotly_chart(
            create_target_chart(data),
            use_container_width=True,
        )

    with tab2:
        st.markdown("### Age distribution")
        st.caption("Explore the age values recorded in the dataset.")
        st.plotly_chart(
            create_age_distribution_chart(data),
            use_container_width=True,
        )

    with tab3:
        st.markdown("### Feature correlation")
        st.caption(
            "Correlation indicates association, not causation."
        )
        st.plotly_chart(
            create_correlation_chart(data),
            use_container_width=True,
        )

    with st.expander("View dataset preview"):
        st.dataframe(data.head(25), use_container_width=True)

except (ValueError, FileNotFoundError, OSError) as exc:
    st.error(f"Could not display dataset insights: {exc}")
