def clamp_count(value, low, high):
    """Clamp value to the inclusive interval from low to high."""
    if type(value) is not int or type(low) is not int or type(high) is not int:
        raise TypeError("value, low, and high must be exact built-in integers")

    minimum = -1_000_000_000
    maximum = 1_000_000_000
    if not (minimum <= value <= maximum):
        raise ValueError("value is outside the allowed range")
    if not (minimum <= low <= maximum):
        raise ValueError("low is outside the allowed range")
    if not (minimum <= high <= maximum):
        raise ValueError("high is outside the allowed range")
    if low > high:
        raise ValueError("low must not exceed high")

    return min(max(value, low), high)
