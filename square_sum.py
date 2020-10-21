def square_sum(numbers):
    """Complete the square sum function so that it squares
    each number passed into it and then sums the results together.
    """
    return sum([pow(n, 2) for n in numbers])