#Codewars
#Write a function that accepts two parameters,
#i) a string (containing a list of words) and ii) an integer (n).
#The function should alphabetize the list based on the nth letter of each word.


def sort_it(list_,n):
    """Alphabetize the list based on the nth letter of each word."""
    to_list = [i.strip() for i in list_.split(",")]
    new_list = sorted(to_list, key=lambda to_list: to_list[n - 1])
    result = ", ".join(new_list)
    return result
