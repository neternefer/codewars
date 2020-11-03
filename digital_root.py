def digital_root(n):
    """Given n, take the sum of the digits of n.
    If that value has more than one digit, continue
    reducing in this way until a single-digit number is produced.
    The input will be a non-negative integer.
    Iterative version:
    def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
    """
    if n % 9 == 0 and n != 0:
        return 9
    return n % 9