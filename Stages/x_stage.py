from Controller.stage_controller import StageController

def home_x(controller: StageController):
    # Switch Modbus 'x' on
    command = controller.add_error_code(':03050427FF00')
    controller.send_cmd(command, True)

    # Switch SERVO on for X axis
    command = controller.add_error_code(':03050403FF00')
    controller.send_cmd(command, True)

    # Home X axis
    command = controller.add_error_code(':0305040BFF00')
    controller.send_cmd(command, True)

    # Homing off command for X axis
    command = controller.add_error_code(':0305040B0000')
    controller.send_cmd(command, True)

    # Check homing status
    homing_completed = False
    while not homing_completed:
        command = controller.add_error_code(':030390050001')
        response, _ = controller.send_cmd(command, True)
        
        if "98F0" in response:
            print("Homing process for X axis completed successfully.")
            homing_completed = True
        else:
            print("Waiting for X axis homing to complete... Response: ", response)

        controller.serial_connection.timeout = 0.5  # Adjust timeout for polling

def move_x(controller: StageController, distance, speed, acceleration):
    # Validate and prepare parameters (example, adjust as needed)
    distance_hex = controller.format_hex(int(distance * 100), 8)  # Convert to desired format
    speed_hex = controller.format_hex(int(speed * 100), 8)
    acceleration_hex = controller.format_hex(int(acceleration * 100), 4)

    # Construct the command with parameters
    command = f':03109900000912{distance_hex}{speed_hex}{acceleration_hex}00000000'
    command_with_checksum = controller.add_error_code(command)

    # Send the command
    controller.send_cmd(command_with_checksum, True)
