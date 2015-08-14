#Write a class that, when given a string, will return an uppercase string
#with each letter shifted forward in the alphabet by however many spots
#the cipher was initialized to.
#If something in the string is not in the alphabet
#(e.g. punctuation, spaces), simply leave it as is.
#Examples:
#c = CaesarCipher(5); # creates a CipherHelper with a shift of five
#c.encode('Codewars') # returns 'HTIJBFWX'
#c.decode('BFKKQJX') # returns 'WAFFLES'

class CaesarCipher(object):
    
    def __init__(self, shift):
        self.shift = shift
        self.alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def encode(self, str1):
        new_str = ""
        str1 = str1.upper()
        for i in str1:
            if i in self.alph:
                index = self.alph.index(i)
                new_str += self.alph[(index + self.shift)%26]
            else:
                new_str += i
        
        return new_str
    
    def decode(self, str1):
        new_str = ""
        str1 = str1.upper()
        for i in str1:
            if i in self.alph:
                index = self.alph.index(i)
                new_str += self.alph[(index - self.shift)%26]
            else:
                new_str += i
        
        return new_str
