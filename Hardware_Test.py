from robot_hat import Pin
from robot_hat import PWM
from time import sleep

led_pin = Pin("D1")                      # create a Pin object from a digital pin
# Initialize PWM on P0 (adjust if needed)
servo_pin = PWM('P0')  
servo_pin.freq(50)  # Set frequency to 50Hz (Servo standard)

def set_servo_angle(angle):
    """
    Move SG90 servo to a specific angle (0-180 degrees)
    by adjusting the servo_pin pulse width.
    """
    if not (0 <= angle <= 180):
        print("Error: Angle must be between 0 and 180 degrees")
        return
    
    # Convert angle to duty cycle (2.5% to 12.5%)
    duty_cycle = (angle / 180) * 10 + 2.5  # Maps 0°-180° to 2.5%-12.5%

    # Apply duty cycle
    servo_pin.pulse_width_percent(duty_cycle)
    print(f"Moved to {angle} degrees (Duty Cycle: {duty_cycle:.1f}%)")

# Sweep servo from 0° to 180° in 30-degree steps
for angle in range(0, 181, 30):
    set_servo_angle(angle)
    time.sleep(0.5)  # Delay for servo movement

# Reset to neutral position (90 degrees)
set_servo_angle(90)

print("Servo setup complete!")
