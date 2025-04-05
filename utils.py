def validate_input(value, min_value, max_value):
    if value < min_value or value > max_value:
        raise ValueError(f"Input must be between {min_value} and {max_value}")
    return value
