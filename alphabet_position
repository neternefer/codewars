#In this kata you are required to, given a string,
#replace every letter with its position in the alphabet.
#If anything in the text isn't a letter,
#ignore it and don't return it. a being 1, b being 2, etc.

def alphabet_position(text):
    text = text.lower()
    new_text = ""
    alph = " abcdefghijklmnopqrstuvwxyz"
    for i in text:
        for j in range(len(alph)):
            if i == alph[j] and i != " " :
                new_text += (str(j) + " ")
            
    return new_text.strip()
