def is_divisible(n,x,y):
    """Create a function that checks if a number n is divisible
        by two numbers x AND y. All inputs are positive, non-zero digits.
    """
    return n % x == 0 and n % y == 0
