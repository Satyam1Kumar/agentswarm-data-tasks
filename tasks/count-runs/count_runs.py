def count_runs(items):
    """Count maximal consecutive groups of equal strings."""
    if type(items) is not list:
        raise TypeError("items must be a built-in list")
    if any(type(item) is not str for item in items):
        raise TypeError("items must contain exact built-in strings")

    if len(items) > 1000:
        raise ValueError("items may contain at most 1000 strings")
    if any(len(item) > 64 for item in items):
        raise ValueError("each string may contain at most 64 code points")

    runs = 0
    for index, item in enumerate(items):
        if index == 0 or item != items[index - 1]:
            runs += 1
    return runs
