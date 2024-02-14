# Gamepad-enabled control of an IAI stage system

This project is aiming to integrate a open-loop gamepad control to our stage system using Python. The stage system from IAI we are using uses a MODBUS ASCI communication protocol. Consequently the code reflects these characteristics. Hence, if another stage system or communication protol is used changes to the commands and the way they are assembled and handled might become necessary. 

# System Information
- Stage System: IAI Stage system
- Controller: PS4 DualShock Controller

# Code Explanations
## x_stage.py

- The home_x function sends a series of commands to the stage to initiate the homing process, waits for the homing to complete, and checks the homing status by sending a command and evaluating the response.
- The move_x function constructs a command to move the X stage, incorporating parameters for distance, speed, and acceleration. It formats these parameters as hexadecimal strings as required by your device's protocol, calculates the command's checksum, and sends the command.
- This example uses placeholder response checks and command strings. You should adjust these based on your specific hardware's documentation.

## y_stage.py

- The structure of y_stage.py mirrors that of x_stage.py, with adjustments made for the specifics of the Y stage (notably the Modbus address prefix changes from :03... for X to :02... for Y).
- The home_y function initiates the homing sequence for the Y axis, following the same pattern of sending commands and checking for completion as shown for the X axis.
- The move_y function constructs a command to move the Y stage, taking into account the provided distance, speed, and acceleration. These values are formatted and incorporated into the command string according to your device's protocol.
- As with the X stage, replace placeholder response checks and command strings with those appropriate for your Y stage's control protocol.


## z_stage.py

- The home_z function sends commands to initiate the Z stage's homing process, waits for completion, and checks the homing status by sending a status request command and interpreting the response.
- The move_z function constructs a move command for the Z stage using provided distance, speed, and acceleration parameters, converts these values to the appropriate format, appends the necessary command structure and checksum, and sends the command to the stage.
- Adjust command strings, response codes, and parameter formatting as necessary to align with your Z stage's specific control protocol and hardware documentation.



## phi_stage.py

- The home_phi function initiates the homing sequence for the Phi axis by sending the appropriate commands, waits for the homing process to complete, and verifies the completion by sending a status request command and evaluating the response.
- The move_phi function creates a command to move the Phi stage, incorporating the provided parameters for distance, speed, and acceleration into the command string, appending the necessary checksum, and sending the command to the stage.
- Command strings, response codes, and the process of formatting parameters should be adjusted based on the specifics of your Phi stage's control protocol and documentation.



## main.py

- Gamepad Initialization: initialize_gamepad sets up the gamepad using pygame, ensuring it's connected and ready to use.
- Polling Gamepad Input: poll_gamepad continuously checks for input from the gamepad. When a button associated with a specific action is pressed, it calls the corresponding function from the stages module to control the stages. This example includes placeholders for other stage control actions (like move_x_increase), which you should implement based on the button mappings and functionality you desire.
- Main Function: The main function initializes the StageController with the appropriate COM port, initializes the gamepad, and enters the polling loop to listen for gamepad inputs. It exits the application when the designated exit button is pressed.
- This script initializes the StageController and gamepad, then enters a loop to continuously poll for gamepad inputs.
- For each stage (X, Y, Z, Phi), there are buttons designated for homing and for increasing/decreasing the stage position. The script checks if these buttons are pressed and calls the corresponding functions from the stages module with appropriate parameters.
- The distances (distance_x, distance_y, distance_z, distance_phi) are adjusted based on the button presses to increase or decrease the position. The step_size variable determines how much the position changes with each button


# Help_Codes

In order to check for the mapping of the controller you are using please use *Gamepad_map.ipynb*

If you are unsure if your controller is correcly recognized and initialised use *Gamepad_init.ipynb*

