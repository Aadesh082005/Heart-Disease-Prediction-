from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Data paths
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

DATASET_PATH = RAW_DATA_DIR / "heart.csv"

# Model paths
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "heart_disease_model.joblib"
METADATA_PATH = MODEL_DIR / "model_metadata.json"

# Reports
REPORTS_DIR = BASE_DIR / "reports"
EVALUATION_PATH = REPORTS_DIR / "model_evaluation.json"

# Common dataset features
FEATURE_COLUMNS = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
]

TARGET_COLUMN = "target"

RANDOM_STATE = 42

# Ensure output directories exist.
for directory in [
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODEL_DIR,
    REPORTS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)