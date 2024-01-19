def hex2bin(hex_string):
    bin_string = ''
    for hex_char in hex_string:
        if hex_char == 'f':
            bin_string += '1111'
        elif hex_char == 'e':
            bin_string += '1110'
        elif hex_char == 'd':
            bin_string += '1101'
        elif hex_char == 'c':
            bin_string += '1100'
        elif hex_char == 'b':
            bin_string += '1011'
        elif hex_char == 'a':
            bin_string += '1010'
        elif hex_char == '9':
            bin_string += '1001'
        elif hex_char == '8':
            bin_string += '1000'
        elif hex_char == '7':
            bin_string += '0111'
        elif hex_char == '6':
            bin_string += '0110'
        elif hex_char == '5':
            bin_string += '0101'
        elif hex_char == '4':
            bin_string += '0100'
        elif hex_char == '3':
            bin_string += '0011'
        elif hex_char == '2':
            bin_string += '0010'
        elif hex_char == '1':
            bin_string += '0001'
        elif hex_char == '0':
            bin_string += '0000'
    return bin_string
