#Write a function that will return the count of distinct case-insensitive
#alphabetic characters that occur more than once in the given string.
#"aabbcdeB" -> 2 # 'a' and 'b'

def duplicate_count(text):
    text = text.lower()
    lst = []
    for letter in text:
        count = text.count(letter)
        if count > 1 and letter not in lst:
            lst.append(letter)
    
    return len(lst)  
        
