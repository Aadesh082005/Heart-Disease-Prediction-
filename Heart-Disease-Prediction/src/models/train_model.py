import json

import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from src.data.preprocessing import (
    clean_dataset,
    load_dataset,
    prepare_features,
)
from src.utils.config import (
    DATASET_PATH,
    EVALUATION_PATH,
    FEATURE_COLUMNS,
    METADATA_PATH,
    MODEL_PATH,
    RANDOM_STATE,
    TARGET_COLUMN,
)


def train_model():
    """Train, evaluate, and save the heart disease classifier."""

    data = load_dataset(DATASET_PATH)
    data = clean_dataset(data)

    X, y = prepare_features(data)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    # Imputation is fitted only on the training data.
    # This prevents test-set information leaking into training.
    model = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median"),
            ),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=200,
                    random_state=RANDOM_STATE,
                    class_weight="balanced",
                ),
            ),
        ]
    )

    model.fit(X_train, y_train)

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
        "test_samples": int(len(y_test)),
    }

    # Save the complete pipeline, including imputation.
    joblib.dump(model, MODEL_PATH)

    metadata = {
        "model_name": "Random Forest Classifier",
        "model_version": "1.0",
        "feature_names": FEATURE_COLUMNS,
        "target_column": TARGET_COLUMN,
        "evaluation_metrics": metrics,
    }

    with open(
        METADATA_PATH,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(metadata, file, indent=4)

    with open(
        EVALUATION_PATH,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(metrics, file, indent=4)

    print("Model training completed.")
    print(f"Model saved to: {MODEL_PATH}")
    print("\nEvaluation metrics:")

    for metric, value in metrics.items():
        print(f"{metric}: {value}")

    return model, metrics


if __name__ == "__main__":
    train_model()