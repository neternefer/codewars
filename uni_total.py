def uni_total(string):
    """(str) -> int
    You'll be given a string, and have to return the total of all the
    unicode characters as an int.
    Should be able to handle any characters sent at it.
    >>> uni_total("aaa")
    291
    """
    #your code here
    result = 0
    for i in string:
        result += ord(i)
    return result
