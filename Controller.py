import pygame  # type: ignore
import time  

# Initialize Pygame
pygame.init()
pygame.joystick.init()

# Check how many joysticks are connected
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("No joystick detected!")
    exit()  # Stop execution if no joystick is found

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.JOYAXISMOTION and event.axis == 0:
            steering = event.value
            if abs(steering) < 0.1:  # Apply a dead zone
                steering = 0

        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 4:  
                LRsignal = -1
                print("Left signal")
            elif event.button == 5:  
                LRsignal = 1
                print("Right signal")
            elif event.button == 0:
                forward = 1
                print("Moving forward")

        elif event.type == pygame.JOYBUTTONUP:
            if event.button in {4, 5}:
                LRsignal = 0
                print("No signal")
            elif event.button == 0:
                forward = 0
                print("Stop moving")

    print(f"Steering: {steering:.2f}")  # Display steering value
    pygame.time.wait(50)  # Small delay to prevent CPU overload

pygame.quit()

