def is_palindrome1(s):
    """(str) -> bool
    Return True if and only if s is a palindrome.
    >>> is_palindrome1('noon')
    True
    >>> is_palindrome1('racecar')
    True
    >>> is_palindrome1('dented')
    False
    """
    return reverse(s) == s

def is_palindrome2(s):
    """(str) -> bool
    Return True if and only if s is a palindrome.
    >>> is_palindrome2('noon')
    True
    >>> is_palindrome2('racecar')
    True
    >>> is_palindrome2('dented')
    False
    """
    n = len(s)
    #Compare the first half of the string to the reverse of the second half.
    #Omit the middle character of an odd-length string.
    return s[:n//2] == reverse(s[n-n//2:])

def is_palindrome3(s):
    """(str) -> bool
    Return True if and only if s is a palindrome.
    >>> is_palindrome3('noon')
    True
    >>> is_palindrome3('racecar')
    True
    >>> is_palindrome3('dented')
    False
    """
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    #In palindrome i and j will either be equal at the end(odd number)
    #or j will be smaller than i -> the middle of the string has been reached.
    #If s == '', i = 0 and j = -1.
    return j <= 1
    
def reverse(s):
    """(str) -> str
    Return the reversed version of s.
    >>> reverse('hell')
    'lleh'
    >>> reverse('a')
    'a'
    """
    rev = ''
    for ch in s:
        rev = ch + rev
    return rev
