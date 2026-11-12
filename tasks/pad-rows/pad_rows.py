"""Create a padded copy of a matrix without mutating its rows."""

def pad_rows(rows: list[list[int]], fill: int) -> list[list[int]]:
    """Pad each row with ``fill`` to the length of the longest row."""
    if type(rows) is not list:
        raise TypeError("rows must be a built-in list")
    if type(fill) is not int:
        raise TypeError("fill must be a built-in int")

    # Check every nested type before checking any lengths or numeric ranges.
    for row in rows:
        if type(row) is not list:
            raise TypeError("each row must be a built-in list")
        for value in row:
            if type(value) is not int:
                raise TypeError("row values must be built-in ints")

    if len(rows) > 100:
        raise ValueError("rows may contain at most 100 rows")
    if any(len(row) > 100 for row in rows):
        raise ValueError("each row may contain at most 100 values")

    values = [fill]
    values.extend(value for row in rows for value in row)
    if any(value < -1_000_000_000 or value > 1_000_000_000 for value in values):
        raise ValueError("values must be between -1000000000 and 1000000000")

    width = max((len(row) for row in rows), default=0)
    return [row + [fill] * (width - len(row)) for row in rows]
