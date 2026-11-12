def middle_chars(text):
    """Return the middle one or two Unicode code points of text."""
    if type(text) is not str:
        raise TypeError("text must be an exact built-in string")
    if len(text) > 1000:
        raise ValueError("text may contain at most 1000 code points")

    middle = len(text) // 2
    if len(text) % 2:
        return text[middle]
    return text[middle - 1:middle + 1]
