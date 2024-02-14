import pygame
from Controller.stage_controller import StageController
from Stages.x_stage import home_x, move_x
from Stages.y_stage import home_y, move_y
from Stages.z_stage import home_z, move_z
from Stages.phi_stage import home_phi, move_phi

def initialize_gamepad():
    pygame.init()
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("No gamepad connected")
        return None
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Gamepad connected: {joystick.get_name()}")
    return joystick

def poll_gamepad(joystick, controller):
    buttons = {
        'home_x': 7,
        'move_x_increase': 14,
        'move_x_decrease': 13,
        'home_y': 8,
        'move_y_increase': 12,
        'move_y_decrease': 11,
        'home_z': 2,
        'move_z_increase': 0,  
        'move_z_decrease': 3,
        'home_phi': 1,
        'move_phi_increase': 9,
        'move_phi_decrease': 10,
        'exit': 15
    }

    # Initial distances and step size
    distance_x = distance_y = distance_z = distance_phi = 0
    step_size = 5  
    speed = 15
    acceleration = 0.5


    running = True
    while running:
        pygame.event.pump()

        if joystick.get_button(buttons['exit']):
            print("Exiting program...")
            running = False

        if joystick.get_button(buttons['home_x']):
            home_x(controller)

        if joystick.get_button(buttons['move_x_increase']):
            distance_x += step_size
            move_x(controller, distance_x, speed, acceleration)  

        if joystick.get_button(buttons['move_x_decrease']):
            distance_x = max(0, distance_x - step_size)
            move_x(controller, distance_x, speed, acceleration)

        if joystick.get_button(buttons['home_y']):
            home_y(controller)

        if joystick.get_button(buttons['move_y_increase']):
            distance_y += step_size
            move_y(controller, distance_y, speed, acceleration)

        if joystick.get_button(buttons['move_y_decrease']):
            distance_y = max(0, distance_y - step_size)
            move_y(controller, distance_y, speed, acceleration)

        if joystick.get_button(buttons['home_z']):
            home_z(controller)

        if joystick.get_button(buttons['move_z_increase']):
            distance_z += step_size
            move_z(controller, distance_z, speed, acceleration)

        if joystick.get_button(buttons['move_z_decrease']):
            distance_z = max(0, distance_z - step_size)
            move_z(controller, distance_z, speed, acceleration)

        if joystick.get_button(buttons['home_phi']):
            home_phi(controller)

        if joystick.get_button(buttons['move_phi_increase']):
            distance_phi += step_size
            move_phi(controller, distance_phi, speed, acceleration)

        if joystick.get_button(buttons['move_phi_decrease']):
            distance_phi = max(0, distance_phi - step_size)
            move_phi(controller, distance_phi, speed, acceleration)

        pygame.time.wait(100)  # Delay to prevent overwhelming the event loop [in ms]

def main():
    com_port = 'COM3'  
    controller = StageController(com_port=com_port)
    joystick = initialize_gamepad()
    if joystick is not None:
        poll_gamepad(joystick, controller)
    pygame.quit()

if __name__ == "__main__":
    main()
