"""
    Return the highest value of consonant substrings.
    a = 1, b = 2, c = 3, .... z = 26...
    For the word "strength", solve("strength") = 57
    -- The consonant substrings are: "str" and "ngth" with 
    values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20
    + 8 = 49. The highest is 57.
"""
import string 

def solve(s):
    scores = set()
    count = 0
    vowels = set('aeiouAEIOU')
    r = ''.join(letter if letter not in vowels else "@" for letter in s)
    for letter in r:
        if letter not in vowels and letter != '@':
            count += (string.ascii_lowercase.index(letter) + 1)
        else:
            scores.add(count)
            count = 0
        scores.add(count)    
    return max(scores)
            
solve("strength")

