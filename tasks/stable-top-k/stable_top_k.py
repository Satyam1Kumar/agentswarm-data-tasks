def stable_top_k(scores, k):
    """Return the first k score indices, with ties kept in input order."""
    if type(scores) is not list or type(k) is not int:
        raise TypeError("scores must be a built-in list and k a built-in int")
    if any(type(score) is not int for score in scores):
        raise TypeError("scores must contain exact built-in ints")

    if len(scores) > 1000:
        raise ValueError("scores may contain at most 1000 values")
    if any(score < -1_000_000_000 or score > 1_000_000_000 for score in scores):
        raise ValueError("scores are outside the supported range")
    if k < 0 or k > len(scores):
        raise ValueError("k must be between zero and the number of scores")

    return sorted(range(len(scores)), key=lambda index: (-scores[index], index))[:k]
