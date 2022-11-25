def bin_to_hex(binary_string):
    # return the hexadecimal representation of the 
    # numerical equivalent of binary_string
    # Good Luck!
    i = int(binary_string, 2)
    return format(i, 'x')
    
def hex_to_bin(hex_string):
    # return the binary representation of the
    # numerical equivalent of hex_string
    # Good Luck!
    return bin(int(hex_string, 16))[2:]
