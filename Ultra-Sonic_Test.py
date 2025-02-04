from robot_hat import Pin
from robot_hat import Ultrasonic
import time

# Define pins
TRIGGER_PIN = "D0"  # Trigger pin
ECHO_PIN = "D1"     # Echo pin

SENSOR = Ultrasonic(Pin(TRIGGER_PIN), Pin(ECHO_PIN, mode=Pin.IN, pull=Pin.PULL_DOWN))
# Main loop: Print distance every second
try:
    while True:
        dist = SENSOR.read
        print(f"Distance: {dist} cm")
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement stopped.")
