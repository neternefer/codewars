import random
def random_case(x):
    """(str) -> str
    Write a function that will randomly upper and lower characters in a string.
    >>>random_case("Donec eleifend cursus lobortis")
    "DONeC ElEifEnD CuRsuS LoBoRTIs"
    """
    result = ""
    for letter in x:
        index = random.randrange(2)
        if index == 1:
            l = letter.upper()
        else:
            l = letter.lower()
        result += l
    return result
