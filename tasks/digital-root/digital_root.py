def digital_root(n):
    """Return the single-digit result of repeatedly summing decimal digits."""
    if type(n) is not int:
        raise TypeError("n must be an exact built-in integer")
    if n < 0 or n > 10**18:
        raise ValueError("n must be between zero and 10**18")

    while n >= 10:
        digit_sum = 0
        while n:
            n, digit = divmod(n, 10)
            digit_sum += digit
        n = digit_sum
    return n
