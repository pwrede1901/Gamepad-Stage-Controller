import time

from sendCMD import send_cmd
from hex2bin import hex2bin
from AddErrorCode import add_error_code

def moveZ(ser, distance, speed, acceleration, timeout):
    # Check Input Values
    if distance > 150 or distance < 0 or speed > 100 or speed < 0:
        print('ERROR: Invalid Position or Speed.')
        return -1

    # Starting register 9900 with 9 registers and 18 bytes
    string1 = ':01109900000912'

    # Distance
    distance = int(distance * 100)
    dist_hex = format(distance, '08X')
    string2 = dist_hex

    # Position band specification register
    string3 = '00000001'

    # Speed specification register
    speed = int(speed * 100)
    sp_hex = format(speed, '08X')
    string4 = sp_hex

    # Acceleration specification register
    acceleration = int(acceleration * 100)
    ac_hex = format(acceleration, '04X')
    string5 = ac_hex

    # Push-current limit values
    string6 = '0000'

    # Control flag
    string7 = '0000'

    # Error check
    checksum = sum([int(string1[i:i+2], 16) for i in range(2, len(string1), 2)])
    checksum += sum([int(string2[i:i+2], 16) for i in range(0, len(string2), 2)])
    checksum += sum([int(string4[i:i+2], 16) for i in range(0, len(string4), 2)])
    checksum += sum([int(string5[i:i+2], 16) for i in range(0, len(string5), 2)])

    comp_2 = format(0xffffffff - checksum + 1, '02X')[-2:]
    string8 = comp_2

    string_def = string1 + string2 + string3 + string4 + string5 + string6 + string7 + string8

    send_cmd(ser, add_error_code(string_def), 1)

    cond = True
    start_time = time.time()

    while cond:
        out, num = send_cmd(ser, ':01039005000166', 1)
        temp = hex2bin(out[7:11])
        if temp[12] == '1':
            cond = False
        time.sleep(0.1)

        # Check for timeout
        if time.time() - start_time > timeout:
            print('Timeout reached.')
            break

    out, num = send_cmd(ser, ':0103900000026A', 1)

    n_bytes = int(out[5:7], 16)  # number of bytes encoding the position
    position = int(out[7:7 + 2 * n_bytes], 16)  # position in 1:100 mm
    position = position / 100  # position in mm

    return position
