def fix_the_meerkat(arr):
    """(arr) -> arr
    Reverse given array.
    >>>fix_the_meerkat(["tail", "body", "head"])
    ["head", "body", "tail"]
    """
    result = []
    for a in reversed(arr):
        result.append(a)
    return result
