def longest(s1, s2):
    """Given two strings, return the longest possible
    string with each letter from s1 and s2 appearing only
    once. Sort alphabetically.
    """
    new_str = ''
    for letter in s1 + s2:
        if letter not in new_str:
            new_str += letter
    return ('').join(sorted(new_str))