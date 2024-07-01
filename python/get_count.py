def get_count(string):
    """
    Return the number of vowels in string.
    """
    return sum(1 for letter in string if letter in "AEIOUaeiou")