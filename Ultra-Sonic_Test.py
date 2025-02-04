from robot_hat import Pin
import time

# Define pins
TRIGGER_PIN = Pin("D0")  # Trigger pin
ECHO_PIN = Pin("D1")     # Echo pin

pulse_end = 0
pulse_start = 0


def get_distance():
    global pulse_end, pulse_start
    """
    Measures the distance using an HC-SR04 ultrasonic sensor.
    Returns distance in centimeters.
    """
    # Ensure trigger pin is low before starting
    TRIGGER_PIN.value(0)
    time.sleep(0.002)  # Small delay

    # Send 10µs HIGH pulse to trigger
    TRIGGER_PIN.value(1)
    time.sleep(0.00001)  # 10µs delay
    TRIGGER_PIN.value(0)

    # Measure the pulse width on echo pin
    while ECHO_PIN.value() == 0:
        pulse_start = time.time()  # Start time
    
    while ECHO_PIN.value() == 1:
        pulse_end = time.time()  # End time

    pulse_duration = pulse_end - pulse_start

    # Convert time to distance (speed of sound = 34300 cm/s)
    distance = (pulse_duration * 34300) / 2

    return round(distance, 2)  # Return rounded distance

# Main loop: Print distance every second
try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist} cm")
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement stopped.")
