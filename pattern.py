#You have to write a function pattern which creates the following pattern
#upto n number of rows. If the Argument is 0 or a Negative Integer
#then it should return "" i.e. empty string.
"""Example:
pattern(4):

1234
234
34
4
"""
def pattern(n):
    l = ""
    index = 0
    result = ""
    
    for i in range(1, n + 1):
        l += str(i)
    if n <= 0:
        return ""
    else:
        while l:
            result += l + "\n"
            l = l[index + 1:]
               
        return result.strip()
