import re

def coffee(sentence):
   
    return re.sub(r"coffee", "COFFEE", sentence, flags=re.IGNORECASE)


