def digitize(n):
    """Given a random non-negative number, you have to
    return the digits of this number within an array in reverse order.
    Fun solution: return map(int, str(n)[::-1])
    """
    return [int(letter) for letter in str(n)][::-1]