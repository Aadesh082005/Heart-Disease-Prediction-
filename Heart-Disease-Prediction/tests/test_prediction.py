import pandas as pd
import pytest

from src.features.feature_engineering import (
    prepare_input_features,
)
from src.utils.config import FEATURE_COLUMNS


def test_prepare_input_features():
    values = {
        feature: 1
        for feature in FEATURE_COLUMNS
    }

    result = prepare_input_features(values)

    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == FEATURE_COLUMNS
    assert len(result) == 1


def test_missing_feature():
    values = {
        feature: 1
        for feature in FEATURE_COLUMNS
    }

    values.pop(FEATURE_COLUMNS[0])

    with pytest.raises(ValueError):
        prepare_input_features(values)


def test_missing_input_value():
    values = {
        feature: 1
        for feature in FEATURE_COLUMNS
    }

    values[FEATURE_COLUMNS[0]] = None

    with pytest.raises(ValueError):
        prepare_input_features(values)