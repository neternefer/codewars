def short_long(a, b):
    """Given 2 strings, a and b, return a string of the form
    short+long+short, with the shorter string on the outside and the
    longer string on the inside. The strings will not be the same length,
    but they may be empty ( length 0 ).
    solution("1", "22") # returns "1221"
    """
    smaller, larger = (a, b) if len(a) < len(b) else (b, a)
    return smaller + larger + smaller