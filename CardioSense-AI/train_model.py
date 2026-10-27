
from pathlib import Path

import joblib
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "dataset" / "heart.csv"
MODEL_DIR = ROOT / "models"

FEATURES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs",
    "restecg", "thalach", "exang", "oldpeak", "slope",
    "ca", "thal"
]


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            "Place heart.csv inside the dataset folder."
        )

    data = pd.read_csv(DATA_PATH)

    required = FEATURES + ["target"]
    missing = [col for col in required if col not in data.columns]

    if missing:
        raise ValueError(f"Missing dataset columns: {missing}")

    data = data[required].dropna()

    X = data[FEATURES]
    y = data["target"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_scaled, y_train)

    predictions = model.predict(X_test_scaled)

    print("Accuracy:", round(
        accuracy_score(y_test, predictions), 4
    ))
    print(classification_report(y_test, predictions))

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, MODEL_DIR / "heart_model.pkl")
    joblib.dump(scaler, MODEL_DIR / "scaler.pkl")

    print("Saved model and scaler in:", MODEL_DIR)


if __name__ == "__main__":
    main()
