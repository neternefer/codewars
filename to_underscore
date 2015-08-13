#Complete the function/method so that it takes CamelCase string
#and returns the string in snake_case notation. Lowercase
#characters can be numbers. If method gets number, it should return string.

def to_underscore(string):
    new_string = ""
    string = str(string)
    for letter in string:
        if letter.isupper():
            new_string += "_" + letter.lower()
        else:
            new_string += letter
    return new_string.strip("_")
