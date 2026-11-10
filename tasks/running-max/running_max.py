def running_max(values):
    """Return the running maximum for each prefix of values."""
    if type(values) is not list:
        raise TypeError("values must be a built-in list")
    if any(type(value) is not int for value in values):
        raise TypeError("values must contain exact built-in integers")

    if len(values) > 1000:
        raise ValueError("values may contain at most 1000 integers")
    if any(value < -1_000_000_000 or value > 1_000_000_000 for value in values):
        raise ValueError("each integer must be within the allowed range")

    result = []
    for value in values:
        if not result or value > result[-1]:
            result.append(value)
        else:
            result.append(result[-1])
    return result
