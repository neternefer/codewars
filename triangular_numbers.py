from math import sqrt
def is_triangle_number(number):
    """
    tr = n(n + 1)/2
    2tr = n(n + 1)
    8tr = 4n(n + 1)
    8tr + 1 = 4n(n + 1) + 1 = 4n^2 + 4n + 1 = (2n + 1)**2
    tr = (sqrt(2n + 1)**2 - 1)/2 = 2n / 2 = n
    """

    if type(number != int:
            return False

    tr = (sqrt(8 * number + 1) - 1) / 2
    if tr == int(tr):
            return True
    return False
