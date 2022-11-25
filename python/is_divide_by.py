def is_divide_by(number, a, b):
    """Your task is to create function to check if an integer
    number is divisible by each out of two arguments.
    (-12, 2, -6)  ->  true
    (-12, 2, -5)  ->  false
    """
    return number % a == 0 and number % b == 0