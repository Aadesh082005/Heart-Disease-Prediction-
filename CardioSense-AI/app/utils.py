
FEATURE_NAMES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs",
    "restecg", "thalach", "exang", "oldpeak", "slope",
    "ca", "thal"
]

FIELD_LIMITS = {
    "age": (1, 120),
    "sex": (0, 1),
    "cp": (0, 3),
    "trestbps": (40, 300),
    "chol": (50, 800),
    "fbs": (0, 1),
    "restecg": (0, 2),
    "thalach": (40, 250),
    "exang": (0, 1),
    "oldpeak": (0, 10),
    "slope": (0, 2),
    "ca": (0, 4),
    "thal": (0, 3),
}


def validate_inputs(form):
    values = []

    for name in FEATURE_NAMES:
        raw_value = form.get(name, "").strip()

        if not raw_value:
            raise ValueError(f"Please enter {name}.")

        try:
            value = float(raw_value)
        except ValueError:
            raise ValueError(
                f"Invalid value for {name}."
            ) from None

        minimum, maximum = FIELD_LIMITS[name]

        if not minimum <= value <= maximum:
            raise ValueError(
                f"{name} must be between {minimum} and {maximum}."
            )

        if name != "oldpeak" and not value.is_integer():
            raise ValueError(
                f"{name} must be a whole number."
            )

        values.append(value)

    return values
