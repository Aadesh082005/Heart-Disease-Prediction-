import joblib

from src.features.feature_engineering import (
    prepare_input_features,
)
from src.utils.config import MODEL_PATH


def load_model():
    """Load the trained model."""

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model file not found. Train the model first."
        )

    return joblib.load(MODEL_PATH)


def predict_heart_disease(input_data):
    """
    Generate a model prediction.

    Returns a dictionary containing the predicted class
    and model-estimated class-1 probability.

    This is an educational model output, not a diagnosis.
    """

    model = load_model()

    features = prepare_input_features(input_data)

    prediction = int(model.predict(features)[0])

    probabilities = model.predict_proba(features)[0]

    classes = list(model.classes_)

    positive_index = classes.index(1)

    probability = float(
        probabilities[positive_index]
    )

    return {
        "prediction": prediction,
        "class_1_probability": probability,
        "model_name": "Random Forest Classifier",
    }