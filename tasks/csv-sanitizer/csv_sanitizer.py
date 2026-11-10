def sanitize_csv_rows(rows):
    """Return independent CSV rows with dangerous formula prefixes neutralized."""
    if type(rows) is not list:
        raise TypeError("rows must be an exact built-in list")

    for row in rows:
        if type(row) is not list:
            raise TypeError("each row must be an exact built-in list")
        for cell in row:
            if type(cell) is not str:
                raise TypeError("each cell must be an exact built-in str")

    ascii_whitespace = " \t\r\n"
    formula_prefixes = "=+-@"
    result = []
    for row in rows:
        sanitized_row = []
        for cell in row:
            index = 0
            while index < len(cell) and cell[index] in ascii_whitespace:
                index += 1
            if index < len(cell) and cell[index] in formula_prefixes:
                sanitized_row.append("'" + cell)
            else:
                sanitized_row.append(cell)
        result.append(sanitized_row)

    return result
