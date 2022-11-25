def grow(arr):
    """Given a non-empty array of integers,
    return the result of multiplying the values together in order.
    Fun solution:
    from functools import reduce
    def grow(arr):
        return reduce(lambda x, y: x * y, arr)
    """
    result = 1
    for i in arr:
        result *= i
    return result