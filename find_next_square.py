import math
def find_next_square(sq):
    '''Return the next square if sq is a square, -1 otherwise'''
    if math.sqrt(sq) - int(math.sqrt(sq)) == 0:
        nextSq = math.floor(math.sqrt(sq)) + 1
        return nextSq * nextSq
    return -1
