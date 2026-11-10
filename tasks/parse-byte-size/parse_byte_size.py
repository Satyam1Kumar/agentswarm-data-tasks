def parse_byte_size(value):
    """Parse a nonnegative ASCII byte size with a binary unit suffix."""
    if type(value) is not str:
        raise TypeError("value must be an exact built-in str")

    units = (
        ("KiB", 1024),
        ("MiB", 1024**2),
        ("GiB", 1024**3),
        ("B", 1),
    )
    for suffix, multiplier in units:
        if value.endswith(suffix):
            digits = value[: -len(suffix)]
            break
    else:
        raise ValueError("invalid byte size")

    if not 1 <= len(digits) <= 9:
        raise ValueError("invalid byte count length")
    if any(char < "0" or char > "9" for char in digits):
        raise ValueError("byte count must contain ASCII digits")
    if len(digits) > 1 and digits[0] == "0":
        raise ValueError("leading zeroes are not allowed")

    return int(digits) * multiplier
