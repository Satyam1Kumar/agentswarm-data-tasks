"""Check whether a bounded non-negative integer is a perfect square."""

import math


def is_perfect_square(n: int) -> bool:
    """Return whether ``n`` is a perfect square in the supported range."""
    if type(n) is not int:
        raise TypeError("n must be an exact built-in int")
    if n < 0 or n > 10**18:
        raise ValueError("n must be between 0 and 10**18")
    root = math.isqrt(n)
    return root * root == n
