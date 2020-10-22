def disemvowel(string):
    """Your task is to write a function that takes a string
    and return a new string with all vowels removed.
    For this kata 'y' isn't considered a vowel."""
    new_str = ''
    for letter in string:
        if letter not in 'aeiouAEIOU':
            new_str += letter
    return new_str