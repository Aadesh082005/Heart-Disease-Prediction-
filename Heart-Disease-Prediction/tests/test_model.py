import numpy as np
from sklearn.pipeline import Pipeline

from src.models.train_model import RandomForestClassifier
from sklearn.impute import SimpleImputer


def test_model_training():
    X = np.array([
        [20, 100],
        [30, 120],
        [40, 130],
        [50, 140],
        [60, 150],
        [70, 160],
    ])

    y = np.array([0, 0, 0, 1, 1, 1])

    model = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=10,
                    random_state=42,
                ),
            ),
        ]
    )

    model.fit(X, y)

    prediction = model.predict([[45, 135]])

    assert prediction[0] in [0, 1]