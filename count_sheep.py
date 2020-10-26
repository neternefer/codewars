def count_sheep(n):
    """Given a non-negative integer, 3 for example,
    return a string with a murmur: "1 sheep...2 sheep...3 sheep...".
    Input will always be valid, i.e. no negative integers.
    """
    return ''.join([str(i) + " sheep..." for i in range(1, n + 1)])