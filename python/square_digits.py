def square_digits(num):
    """Welcome. In this kata, you are asked to square every digit
    of a number and concatenate them."""
    return int(('').join(list(str(int(n) * int(n)) for n in str(num))))