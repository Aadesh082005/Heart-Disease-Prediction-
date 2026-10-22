def format_percentage(value):
    """Format a decimal value as a percentage."""

    return f"{value * 100:.2f}%"


def validate_numeric_range(
    value,
    minimum,
    maximum,
    field_name,
):
    """Validate a numeric value against an allowed range."""

    if not minimum <= value <= maximum:
        raise ValueError(
            f"{field_name} must be between "
            f"{minimum} and {maximum}."
        )

    return value