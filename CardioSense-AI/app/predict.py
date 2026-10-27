
from pathlib import Path

import joblib
import numpy as np

from app.utils import FEATURE_NAMES


ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "heart_model.pkl"
SCALER_PATH = ROOT / "models" / "scaler.pkl"


def load_artifacts():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Missing models/heart_model.pkl. "
            "Copy your existing trained model into models/."
        )

    if not SCALER_PATH.exists():
        raise FileNotFoundError(
            "Missing models/scaler.pkl. "
            "Copy your existing scaler into models/."
        )

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    return model, scaler


def predict_heart_risk(values):
    if len(values) != len(FEATURE_NAMES):
        raise ValueError("Exactly 13 features are required.")

    model, scaler = load_artifacts()

    features = np.asarray(
        values, dtype=float
    ).reshape(1, -1)

    scaled_features = scaler.transform(features)
    prediction = int(model.predict(scaled_features)[0])

    risk_score = None

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(scaled_features)[0]
        classes = list(model.classes_)

        if 1 in classes:
            risk_score = round(
                float(probabilities[classes.index(1)]) * 100,
                1
            )

    return {
        "prediction": prediction,
        "risk_score": risk_score,
    }
