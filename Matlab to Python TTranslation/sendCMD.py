def send_cmd(ser, string1, display):
    try:
        # Check if the port is already open
        if not ser.is_open:
            ser.open()

        # Add colon to the hex string and Terminator Chars
        hex_string = ":" + string1 + '\x0D\x0A'

        # Send command
        ser.write(hex_string.encode())

        # Read response
        response = ser.readline().decode().strip()

        # Display
        if display:
            print(f"String sent to Device: \"{hex_string}\"")
            print(f"Response from Device (in HEX): \"{response}\"")
            print(f"Number of Chars received: {len(response)} (+2 terminator chars)")
            print('-')

        return response  # Return the response

    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # Return None if an error occurs

    finally:
        # Close serial port
        if ser.is_open:
            ser.close()
            print("Serial port closed.")