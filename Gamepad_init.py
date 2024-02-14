## Author: Paul Wrede
## Last Change: 14.02.2024
## Short Description: Useful to check if the Gamepad is actually initilised and detected from the PC

######################################################################################################################################

import pygame
import time

# Initialize Pygame and the joystick module
pygame.init()
pygame.joystick.init()

# Setup
joystick_detected = False
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)  # Get the first joystick
    joystick.init()
    print(f"Joystick initialized: {joystick.get_name()}")
    joystick_detected = True
else:
    print("No joystick detected")

def process_joystick_input():
    # Read analog sticks: Axis 0 and 1 for the left stick, 2 and 3 for the right stick
    left_stick_x = joystick.get_axis(0)
    left_stick_y = joystick.get_axis(1)
    right_stick_x = joystick.get_axis(2)
    right_stick_y = joystick.get_axis(3)

    # For demonstration, print out the values
    print(f"Left Stick X: {left_stick_x:.2f}, Y: {left_stick_y:.2f}")
    print(f"Right Stick X: {right_stick_x:.2f}, Y: {right_stick_y:.2f}")

    # Here, add your code to map these joystick positions to stage movements

# Main loop
try:
    while joystick_detected:
        pygame.event.pump()  # Process event queue
        process_joystick_input()
        time.sleep(0.1)  # Adding a small delay to make the output readable
except KeyboardInterrupt:
    print("Program exited")

pygame.quit()
