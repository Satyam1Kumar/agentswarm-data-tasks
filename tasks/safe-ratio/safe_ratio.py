def safe_ratio(numerator: int, denominator: int) -> float | None:
    """Return the ratio of two bounded exact integers, or None for zero."""
    if type(numerator) is not int or type(denominator) is not int:
        raise TypeError("numerator and denominator must be exact built-in ints")

    lower = -1_000_000_000
    upper = 1_000_000_000
    if not lower <= numerator <= upper or not lower <= denominator <= upper:
        raise ValueError("numerator and denominator are outside the supported range")

    if denominator == 0:
        return None

    return numerator / denominator
