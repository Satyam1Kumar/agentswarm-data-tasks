def split_at(items, index):
    """Return independent prefix and suffix lists split at index."""
    if type(items) is not list or type(index) is not int:
        raise TypeError("items must be a built-in list and index a built-in int")
    if any(type(item) is not str for item in items):
        raise TypeError("items must contain exact built-in strings")

    if len(items) > 1000:
        raise ValueError("items may contain at most 1000 strings")
    if any(len(item) > 64 for item in items):
        raise ValueError("each string may contain at most 64 code points")
    if index < 0 or index > len(items):
        raise ValueError("index must be between zero and the list length")

    return [items[:index], items[index:]]
