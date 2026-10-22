import pandas as pd

from src.utils.config import FEATURE_COLUMNS


def prepare_input_features(input_data):
    """
    Prepare user input in the exact order expected by the model.

    input_data can be a dictionary or pandas DataFrame.
    """

    if isinstance(input_data, dict):
        input_data = pd.DataFrame([input_data])

    if not isinstance(input_data, pd.DataFrame):
        raise TypeError(
            "Input must be a dictionary or pandas DataFrame."
        )

    missing_columns = [
        column
        for column in FEATURE_COLUMNS
        if column not in input_data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing input features: {missing_columns}"
        )

    features = input_data[FEATURE_COLUMNS].copy()

    features = features.apply(
        pd.to_numeric,
        errors="raise",
    )

    if features.isna().any().any():
        raise ValueError(
            "Input features cannot contain missing values."
        )

    return features