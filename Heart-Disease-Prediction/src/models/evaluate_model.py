import json

import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split

from src.data.preprocessing import (
    clean_dataset,
    load_dataset,
    prepare_features,
)
from src.utils.config import (
    DATASET_PATH,
    EVALUATION_PATH,
    MODEL_PATH,
    RANDOM_STATE,
)


def evaluate_model():
    """Evaluate the saved model on a reproducible held-out split."""

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Trained model not found. Train the model first."
        )

    data = clean_dataset(
        load_dataset(DATASET_PATH)
    )

    X, y = prepare_features(data)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    model = joblib.load(MODEL_PATH)

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    metrics = {
        "accuracy": float(
            accuracy_score(y_test, predictions)
        ),
        "precision": float(
            precision_score(
                y_test,
                predictions,
                zero_division=0,
            )
        ),
        "recall": float(
            recall_score(
                y_test,
                predictions,
                zero_division=0,
            )
        ),
        "f1_score": float(
            f1_score(
                y_test,
                predictions,
                zero_division=0,
            )
        ),
        "roc_auc": float(
            roc_auc_score(y_test, probabilities)
        ),
        "confusion_matrix": confusion_matrix(
            y_test,
            predictions,
        ).tolist(),
    }

    EVALUATION_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        EVALUATION_PATH,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(metrics, file, indent=4)

    print(json.dumps(metrics, indent=4))

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0,
        )
    )

    return metrics


if __name__ == "__main__":
    evaluate_model()