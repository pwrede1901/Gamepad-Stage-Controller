import serial
import time

class StageController:
    def __init__(self, com_port='COM3', baudrate=115200):
        self.com_port = com_port
        self.baudrate = baudrate
        self.serial_connection = None

    def open_serial_connection(self):
        if self.serial_connection is None or not self.serial_connection.isOpen():
            self.serial_connection = serial.Serial(port=self.com_port,
                                                   baudrate=self.baudrate,
                                                   parity=serial.PARITY_NONE,
                                                   stopbits=serial.STOPBITS_ONE,
                                                   bytesize=serial.EIGHTBITS,
                                                   timeout=0.1)
            print(f"Opened serial connection on {self.com_port}.")

    def close_serial_connection(self):
        if self.serial_connection and self.serial_connection.isOpen():
            self.serial_connection.close()
            print("Closed serial connection.")

    def send_cmd(self, command, display=False):
        self.open_serial_connection()
        to_send = command.encode() + b'\r\n'
        self.serial_connection.write(to_send)
        time.sleep(0.5)  # Delay for response
        response = self.serial_connection.read(self.serial_connection.in_waiting or 1).decode('utf-8')
        num = len(response)
        if num == 0:
            print('Timeout was reached.')
        elif display:
            print(f'String sent to Device: "{command}"')
            print(f'Response from Device (in HEX): "{response.strip()}"')
            print(f'Number of Chars received: {num - 2} (+2 terminator chars)')
        return response, num

    def add_error_code(self, string):
        if len(string) % 2 == 0:
            print('Error: Input string length must be odd.')
            return -1
        temp = 0x100000000  # Equivalent to hex2dec('ffffffff') + 1
        string = string[1:]  # Remove the first character
        for i in range(0, len(string) - 1, 2):
            temp -= int(string[i:i+2], 16)
        temp_hex = '{:X}'.format(temp)
        complete_string = ':' + string + temp_hex[-2:]
        return complete_string

    def format_hex(self, value, length):
        """Format the given value as a hexadecimal string of the specified length."""
        return f'{value:0{length}X}'

    def calculate_checksum(self, command):
        """Calculate the two's complement checksum for the given command."""
        sum_bytes = sum(int(command[i:i+2], 16) for i in range(1, len(command), 2))  # Start from 1 to skip ':'
        checksum = (0x10000 - sum_bytes) & 0xFFFF
        return self.format_hex(checksum, 4)[-2:]
