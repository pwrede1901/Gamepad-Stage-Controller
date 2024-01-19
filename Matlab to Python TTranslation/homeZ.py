import time
from sendCMD import send_cmd
from hex2bin import hex2bin

def homeZ(ser):
    try:
        # Switch Modbus 'z' on
        send_cmd(ser, ':01050427FF00', display=True)

        # Switch SERVO on
        send_cmd(ser, ':01050403FF00', display=True)

        # Home Device
        send_cmd(ser, ':0105040BFF00', display=True)

        # Homing off
        send_cmd(ser, ':0105040B0000', display=True)

        cond = True

        while cond:
            response = send_cmd(ser, ':010390050001', display=True)
            temp = hex2bin(response[6:10])

            if temp[11] == '1':
                cond = False

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        return 1