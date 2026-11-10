def coalesce_ranges(ranges):
    """Return the sorted union of bounded half-open integer ranges."""
    if type(ranges) is not list:
        raise TypeError("ranges must be an exact built-in list")

    for interval in ranges:
        if type(interval) is not list:
            raise TypeError("each range must be an exact built-in list")
        for endpoint in interval:
            if type(endpoint) is not int:
                raise TypeError("range endpoints must be exact built-in ints")

    if len(ranges) > 1000:
        raise ValueError("at most 1000 ranges are allowed")

    lower = -1_000_000_000
    upper = 1_000_000_000
    nonempty = []
    for interval in ranges:
        if len(interval) != 2:
            raise ValueError("each range must contain exactly two endpoints")

        start, end = interval
        if not lower <= start <= upper or not lower <= end <= upper:
            raise ValueError("range endpoints are outside the supported bounds")
        if start > end:
            raise ValueError("range start must not exceed its end")
        if start < end:
            nonempty.append((start, end))

    nonempty.sort()
    merged = []
    for start, end in nonempty:
        if merged and start <= merged[-1][1]:
            if end > merged[-1][1]:
                merged[-1][1] = end
        else:
            merged.append([start, end])

    return merged
