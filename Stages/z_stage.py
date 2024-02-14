from Controller.stage_controller import StageController

def home_z(controller: StageController):
    # Switch Modbus 'z' on
    command = controller.add_error_code(':01050427FF00')
    controller.send_cmd(command, True)

    # Switch SERVO on for Z axis
    command = controller.add_error_code(':01050403FF00')
    controller.send_cmd(command, True)

    # Home Z axis
    command = controller.add_error_code(':0105040BFF00')
    controller.send_cmd(command, True)

    # Homing off command for Z axis
    command = controller.add_error_code(':0105040B0000')
    controller.send_cmd(command, True)

    # Check homing status
    homing_completed = False
    while not homing_completed:
        command = controller.add_error_code(':010390050001')
        response, _ = controller.send_cmd(command, True)
        
        if "98F2" in response:  # This response code might need adjustment
            print("Homing process for Z axis completed successfully.")
            homing_completed = True
        else:
            print("Waiting for Z axis homing to complete... Response: ", response)

        controller.serial_connection.timeout = 0.5  # Adjust timeout for polling if necessary

def move_z(controller: StageController, distance, speed, acceleration):
    # Validate and prepare parameters
    distance_hex = controller.format_hex(int(distance * 100), 8)  # Adjust format as needed
    speed_hex = controller.format_hex(int(speed * 100), 8)
    acceleration_hex = controller.format_hex(int(acceleration * 100), 4)

    # Construct the command with parameters
    command = f':01109900000912{distance_hex}{speed_hex}{acceleration_hex}00000000'
    command_with_checksum = controller.add_error_code(command)

    # Send the command
    controller.send_cmd(command_with_checksum, True)
