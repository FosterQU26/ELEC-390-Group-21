import pygame # type: ignore
#from picarx import Picarx # type: ignore
import time

#initilize a Picarx object
#px = Picarx()

# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Check how many joysticks are connected
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("No joystick detected!")
else:
    # Initialize the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick {joystick.get_name()} initialized.")

running = True
LRsignal = 0
forward = 0
steering = 0


while running:
    # Process events
    time.sleep(0.5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYAXISMOTION and event.axis == 0:
            steering = event.value

        # Detect button presses
        elif event.type == pygame.JOYBUTTONDOWN and (event.button == 4 or event.button == 5):
            print(f"Button {event.button} pressed.")
            if event.button == 4:
                LRsignal = -1
            else:
                LRsignal = 1

        # Detect button releases
        elif event.type == pygame.JOYBUTTONUP and (event.button == 4 or event.button == 5):
            print(f"Button {event.button} released.")
            LRsignal = 0

        elif event.type == pygame.JOYBUTTONDOWN and (event.button == 0):
            forward = 1

        elif event.type == pygame.JOYBUTTONUP and (event.button == 0):
            forward = 0
    


    # Check LR signal
    match LRsignal:
        case -1:
            print("Left signal")
        case 1:
            print("Right signal")
        case 0:
            print("No signal")
        case _:
            print("Invalid signal") 

    # Check forward signal
    if (forward == 1):
        print("Moving forward")
    else:
        print("Stop moving")

    # Check steering signal
    print(steering)

# Cleanup
pygame.quit()


