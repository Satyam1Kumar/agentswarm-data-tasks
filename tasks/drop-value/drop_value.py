"""Return a fresh list with every occurrence of a value removed."""


def drop_value(items: list[int], value: int) -> list[int]:
    """Return the items that are not equal to value, preserving their order."""
    if type(items) is not list:
        raise TypeError("items must be a built-in list")
    if type(value) is not int:
        raise TypeError("value must be a built-in int")
    if any(type(item) is not int for item in items):
        raise TypeError("items must contain only built-in ints")

    if len(items) > 1000:
        raise ValueError("items may contain at most 1000 values")
    if not -1_000_000_000 <= value <= 1_000_000_000:
        raise ValueError("value is outside the allowed range")
    if any(not -1_000_000_000 <= item <= 1_000_000_000 for item in items):
        raise ValueError("an item is outside the allowed range")

    return [item for item in items if item != value]
