def add_error_code(string):
    if len(string) % 2 == 0:
        print('Error: Input string length must be odd.')
        complete_string = -1
    else:
        temp = int('ffffffff', 16) + 1
        string = string[1:]

        for i in range(0, len(string) - 1, 2):
            temp -= int(string[i:i+2], 16)

        temp = format(temp, 'x')
        complete_string = f':{string}{temp[-2:]}'

    return complete_string