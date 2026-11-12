def mirror_matrix(rows):
    """Return a fresh matrix with each row mirrored left to right."""
    if type(rows) is not list:
        raise TypeError("rows must be a built-in list")
    if any(type(row) is not list for row in rows):
        raise TypeError("each row must be a built-in list")
    if any(type(value) is not int for row in rows for value in row):
        raise TypeError("matrix entries must be exact built-in integers")

    if len(rows) > 100:
        raise ValueError("matrix may contain at most 100 rows")
    if any(len(row) > 100 for row in rows):
        raise ValueError("rows may contain at most 100 entries")
    if rows and any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("matrix rows must all have the same length")
    if any(not -1_000_000_000 <= value <= 1_000_000_000 for row in rows for value in row):
        raise ValueError("matrix entries are outside the allowed range")

    return [row[::-1] for row in rows]
