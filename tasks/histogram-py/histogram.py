from bisect import bisect_right


_MIN_SAFE_INT = -9_007_199_254_740_991
_MAX_SAFE_INT = 9_007_199_254_740_991


def histogram(values, edges):
    """Count values in increasing integer bins, including the last upper edge."""
    if type(values) is not list or type(edges) is not list:
        raise TypeError("values and edges must be exact built-in lists")

    if any(type(value) is not int for value in values):
        raise TypeError("values must contain exact built-in ints")
    if any(type(edge) is not int for edge in edges):
        raise TypeError("edges must contain exact built-in ints")

    if any(value < _MIN_SAFE_INT or value > _MAX_SAFE_INT for value in values):
        raise ValueError("values are outside the supported range")
    if any(edge < _MIN_SAFE_INT or edge > _MAX_SAFE_INT for edge in edges):
        raise ValueError("edges are outside the supported range")
    if len(edges) < 2:
        raise ValueError("at least two edges are required")
    if any(edges[index] >= edges[index + 1] for index in range(len(edges) - 1)):
        raise ValueError("edges must be strictly increasing")

    counts = [0] * (len(edges) - 1)
    for value in values:
        if value == edges[-1]:
            counts[-1] += 1
            continue

        bin_index = bisect_right(edges, value) - 1
        if 0 <= bin_index < len(counts):
            counts[bin_index] += 1

    return counts
