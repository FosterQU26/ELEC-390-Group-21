import pygame # type: ignore
import time

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
DPad = (0, 0)
LRsignal = 0

while running:
    # Process events
    time.sleep(0.5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Detect D-pad movement
        elif event.type == pygame.JOYHATMOTION:
            #print(f"D-pad moved to {event.value}")
            DPad = event.value
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
    
    # Check D-pad movement
    match DPad:
        case (-1, 1):
            print("D-pad moved UP-LEFT")
        case (1, 1):
            print("D-pad moved UP-RIGHT")
        case (-1, -1):
            print("D-pad moved DOWN-LEFT")
        case (1, -1):
            print("D-pad moved DOWN-RIGHT")
        case (0, 1):
            print("D-pad moved UP")
        case (0, -1):
            print("D-pad moved DOWN")
        case (-1, 0):
            print("D-pad moved LEFT")
        case (1, 0):
            print("D-pad moved RIGHT")
        case _:
            print("D-pad in neutral position")

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

# Cleanup
pygame.quit()


