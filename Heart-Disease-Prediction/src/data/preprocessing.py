import pandas as pd

from src.utils.config import FEATURE_COLUMNS, TARGET_COLUMN


def load_dataset(file_path):
    """Load a CSV dataset."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        ) from exc


def validate_dataset(data):
    """Check whether the dataset contains required columns."""

    if data.empty:
        raise ValueError("The dataset is empty.")

    required_columns = FEATURE_COLUMNS + [TARGET_COLUMN]

    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if data[required_columns].isna().all(axis=None):
        raise ValueError("The dataset contains no usable values.")

    return True


def clean_dataset(data):
    """Clean and validate the dataset."""

    data = data.copy()

    validate_dataset(data)

    required_columns = FEATURE_COLUMNS + [TARGET_COLUMN]

    data = data[required_columns]

    for column in required_columns:
        data[column] = pd.to_numeric(
            data[column],
            errors="coerce",
        )

    # Missing target labels cannot be used for supervised training.
    data = data.dropna(subset=[TARGET_COLUMN])

    # Validate target labels.
    data = data[data[TARGET_COLUMN].isin([0, 1])]

    if data.empty:
        raise ValueError(
            "No valid training rows remain after cleaning."
        )

    # Remove rows with missing feature values.
    # The model-training pipeline will handle any remaining
    # missing values in the features.
    return data.reset_index(drop=True)


def prepare_features(data):
    """Separate features and target."""

    validate_dataset(data)

    X = data[FEATURE_COLUMNS].copy()
    y = data[TARGET_COLUMN].copy()

    if X.empty:
        raise ValueError("No feature rows available.")

    if y.nunique() < 2:
        raise ValueError(
            "Training data must contain both target classes."
        )

    return X, y