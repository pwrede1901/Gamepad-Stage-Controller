from Controller.stage_controller import StageController

def home_phi(controller: StageController):
    # Switch Modbus 'phi' on
    command = controller.add_error_code(':04050427FF00')
    controller.send_cmd(command, True)

    # Switch SERVO on for Phi axis
    command = controller.add_error_code(':04050403FF00')
    controller.send_cmd(command, True)

    # Home Phi axis
    command = controller.add_error_code(':0405040BFF00')
    controller.send_cmd(command, True)

    # Homing off command for Phi axis
    command = controller.add_error_code(':0405040B0000')
    controller.send_cmd(command, True)

    # Check homing status
    homing_completed = False
    while not homing_completed:
        command = controller.add_error_code(':040390050001')
        response, _ = controller.send_cmd(command, True)
        
        if "98EF" in response:  # Adjust based on your device's homing completion response for Phi
            print("Homing process for Phi axis completed successfully.")
            homing_completed = True
        else:
            print("Waiting for Phi axis homing to complete... Response: ", response)

        controller.serial_connection.timeout = 0.5  # Adjust timeout for polling if necessary

def move_phi(controller: StageController, distance, speed, acceleration):
    # Validate and prepare parameters
    distance_hex = controller.format_hex(int(distance * 100), 8)  # Adjust format as needed
    speed_hex = controller.format_hex(int(speed * 100), 8)
    acceleration_hex = controller.format_hex(int(acceleration * 100), 4)

    # Construct the command with parameters
    command = f':04109900000912{distance_hex}{speed_hex}{acceleration_hex}00000000'
    command_with_checksum = controller.add_error_code(command)

    # Send the command
    controller.send_cmd(command_with_checksum, True)
