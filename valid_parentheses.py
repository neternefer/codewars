def valid_parentheses(string):
    """(str) -> bool
    Write a function called validParentheses that takes a string of parentheses, and determines if the order of the parentheses is valid. validParentheses
    should return true if the string is valid, and false if it's invalid.
    >>>valid_parentheses( ")(()))" )
    False
    """
    new_string = string
    while len(string) > 2:
        if new_string[0] == '(' and new_string[-1] == ')':
            new_string = string[1:-2]
        else:
            return False
    return True
