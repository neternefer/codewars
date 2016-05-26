import urllib
def generate_link(user):
    """
    urllib.quote(string[, safe])
    Replace special characters in string using the %xx escape. Letters, digits, and the characters '_.-' are never quoted. By default, this function is intended for quoting the path section of the URL.The optional safe parameter specifies additional characters that should not be quoted — its default value is '/'
    That means passing '' for safe will solve your first issue:

    >>> urllib.quote('/test')
    '/test'
    >>> urllib.quote('/test', safe='')
    '%2Ftest'
    """
    
    return 'http://www.codewars.com/users/' + urllib.quote(user, safe = '/')
