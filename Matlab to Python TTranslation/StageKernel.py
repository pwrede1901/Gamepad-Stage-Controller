import serial
import time

from homeZ import home_z

def stage_kernel(arg):
    if arg == 'connect':
        try:
            # Close any existing serial connections
            ser = serial.Serial('COM3')
            ser.close()
            time.sleep(1)  # Wait for any lingering processes to close

            # Initialize the serial connection
            ser = serial.Serial(
                port='COM3',
                baudrate=115200,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=0.1,
                xonxoff=False,
                rtscts=False,
                dsrdtr=False
            )

            # Home Z
            return_value = home_z(ser)
            success = True

        except Exception as e:
            print(f"Error: {e}")
            success = False

        return success, ser

    elif arg == 'disconnect':
        time.sleep(1)  # Wait for any lingering processes to close
        success = True
        return success