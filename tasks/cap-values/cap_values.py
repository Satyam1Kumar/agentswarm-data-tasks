def cap_values(items, limit):
    """Return a new list with each value capped at limit."""
    if type(items) is not list or type(limit) is not int:
        raise TypeError("items must be a built-in list and limit a built-in integer")
    if any(type(item) is not int for item in items):
        raise TypeError("items must contain exact built-in integers")

    if len(items) > 1000:
        raise ValueError("items may contain at most 1000 integers")
    if not -1_000_000_000 <= limit <= 1_000_000_000:
        raise ValueError("limit is outside the allowed range")
    if any(not -1_000_000_000 <= item <= 1_000_000_000 for item in items):
        raise ValueError("an item is outside the allowed range")

    return [min(item, limit) for item in items]
