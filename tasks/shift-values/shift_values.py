def shift_values(items, delta):
    """Return a new list with delta added to every input value."""
    if type(items) is not list or type(delta) is not int:
        raise TypeError("items must be a built-in list and delta a built-in integer")
    if any(type(item) is not int for item in items):
        raise TypeError("items must contain exact built-in integers")

    if len(items) > 1000:
        raise ValueError("items may contain at most 1000 integers")
    if not -1_000_000_000 <= delta <= 1_000_000_000:
        raise ValueError("delta is outside the allowed range")
    if any(not -1_000_000_000 <= item <= 1_000_000_000 for item in items):
        raise ValueError("an item is outside the allowed range")

    return [item + delta for item in items]
