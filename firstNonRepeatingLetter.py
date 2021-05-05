'''
Write a function named first_non_repeating_letter
that takes a string input, and returns the first
character that is not repeated anywhere in the string.
'''
def first_non_repeating_letter(string):
    count = [string.lower().count(letter) for letter in string.lower()]
    return string[count.index(1)] if 1 in count else ''

