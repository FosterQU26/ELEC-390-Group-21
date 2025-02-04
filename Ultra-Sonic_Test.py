from robot_hat import Pin
from robot_hat import Ultrasonic
import time

# Define pins
TRIGGER_PIN = Pin("D0")  # Trigger pin
ECHO_PIN = Pin("D1")     # Echo pin

SENSOR = Ultrasonic(TRIGGER_PIN, ECHO_PIN)
# Main loop: Print distance every second
try:
    while True:
        dist = SENSOR.read
        print(f"Distance: {dist} cm")
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement stopped.")
