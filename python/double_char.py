def double_char(s):
    """Given a string, you have to return a string in which
    each character (case-sensitive) is repeated once.
    double_char("String") ==> "SSttrriinngg"
    """
    return "".join(letter * 2 for letter in s)