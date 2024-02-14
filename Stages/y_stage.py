from Controller.stage_controller import StageController

def home_y(controller: StageController):
    # Switch Modbus 'y' on
    command = controller.add_error_code(':02050427FF00')
    controller.send_cmd(command, True)

    # Switch SERVO on for Y axis
    command = controller.add_error_code(':02050403FF00')
    controller.send_cmd(command, True)

    # Home Y axis
    command = controller.add_error_code(':0205040BFF00')
    controller.send_cmd(command, True)

    # Homing off command for Y axis
    command = controller.add_error_code(':0205040B0000')
    controller.send_cmd(command, True)

    # Check homing status
    homing_completed = False
    while not homing_completed:
        command = controller.add_error_code(':020390050001')
        response, _ = controller.send_cmd(command, True)
        
        if "98F1" in response:  # Adjust based on your device's homing completion response
            print("Homing process for Y axis completed successfully.")
            homing_completed = True
        else:
            print("Waiting for Y axis homing to complete... Response: ", response)

        controller.serial_connection.timeout = 0.5  # Adjust timeout for polling

def move_y(controller: StageController, distance, speed, acceleration):
    # Validate and prepare parameters
    distance_hex = controller.format_hex(int(distance * 100), 8)  # Convert to desired format
    speed_hex = controller.format_hex(int(speed * 100), 8)
    acceleration_hex = controller.format_hex(int(acceleration * 100), 4)

    # Construct the command with parameters
    command = f':02109900000912{distance_hex}{speed_hex}{acceleration_hex}00000000'
    command_with_checksum = controller.add_error_code(command)

    # Send the command
    controller.send_cmd(command_with_checksum, True)
