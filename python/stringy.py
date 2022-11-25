def stringy(size):
    """write me a function stringy that takes a size and returns a
    string of alternating '1s' and '0s'.
    The string should start with a 1.
    A string with size 6 should return :'101010'.
    """
    return ''.join('1' if i % 2 == 0 else '0' for i in range(size))