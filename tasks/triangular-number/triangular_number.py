def triangular_number(n):
    """Return the nth triangular number using exact integer arithmetic."""
    if type(n) is not int:
        raise TypeError("n must be an exact built-in integer")
    if n < 0 or n > 1_000_000_000:
        raise ValueError("n must be between 0 and 1_000_000_000")
    return n * (n + 1) // 2
