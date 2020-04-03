#A simple substitution cipher replaces one character from an alphabet
#with a character from an alternate alphabet, where each character's position
#in an alphabet is mapped to the alternate alphabet for encoding or decoding.
#If a character provided is not in the opposing alphabet, simply leave it as be.

class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2
    
    def encode(self, string):
        new_string = ""
        index = 0
        for i in string:
            if i in map1:
                index = map1.index(i)
                new_string += map2[index]
            else:
                new_string += i
                
        string = new_string
        return string
    
    def decode(self, string):
        new_string = ""
        index = 0
        for i in string:
            if i in map2:
                index = map2.index(i)
                new_string += map1[index]
            else:
                new_string += i
                
        string = new_string
        
        return string
