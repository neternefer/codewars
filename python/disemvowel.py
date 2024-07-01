def disemvowel(string):
    """Your task is to write a function that takes a string
    and return a new string with all vowels removed.
    For this kata 'y' isn't considered a vowel."""
    
    return "".join(letter for letter in string if letter.lower() not in 'aeiou')