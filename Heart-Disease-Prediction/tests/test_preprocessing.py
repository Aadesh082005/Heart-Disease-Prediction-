import pandas as pd
import pytest

from src.data.preprocessing import (
    clean_dataset,
    validate_dataset,
)
from src.utils.config import (
    FEATURE_COLUMNS,
    TARGET_COLUMN,
)


def sample_dataset():
    data = {
        column: [1, 2, 3]
        for column in FEATURE_COLUMNS
    }

    data[TARGET_COLUMN] = [0, 1, 0]

    return pd.DataFrame(data)


def test_valid_dataset():
    data = sample_dataset()

    assert validate_dataset(data) is True


def test_missing_column():
    data = sample_dataset()

    data = data.drop(
        columns=[FEATURE_COLUMNS[0]]
    )

    with pytest.raises(ValueError):
        validate_dataset(data)


def test_clean_dataset():
    data = sample_dataset()

    cleaned = clean_dataset(data)

    assert not cleaned.empty
    assert TARGET_COLUMN in cleaned.columns
    assert len(cleaned) == 3