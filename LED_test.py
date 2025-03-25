from robot_hat import PWM
import time

# Create PWM objects for each pin
pwm4 = PWM('P0')  # Pin 4
pwm5 = PWM('P1')  # Pin 5
pwm6 = PWM('P2')  # Pin 6

# Set frequency and prescaler for each PWM pin (example values)
freq = 1000  # Frequency in Hz
prescaler = 0  # Prescaler value (0-255, typically for adjusting the frequency)
period = 1000  # Period (this can vary depending on your needs)
pulse_width = 500  # Pulse width in microseconds (for on-time duration)
pulse_width_percent = 50  # Duty cycle in percentage (0-100)

# Initialize the PWM settings for each pin
pwm4.freq(freq)
pwm4.prescaler(prescaler)
pwm4.period(period)
pwm4.pulse_width_percent(pulse_width_percent)

pwm5.freq(freq)
pwm5.prescaler(prescaler)
pwm5.period(period)
pwm5.pulse_width_percent(pulse_width_percent)

pwm6.freq(freq)
pwm6.prescaler(prescaler)
pwm6.period(period)
pwm6.pulse_width_percent(pulse_width_percent)

# Function to sequentially turn on LEDs with 2-second delay
def test_leds():
    pwm4.pulse_width_percent(100)  # Turn on pin 4
    print("Pin 4 ON")
    time.sleep(2)  # Wait for 2 seconds
    
    pwm4.pulse_width_percent(0)  # Turn off pin 4
    pwm5.pulse_width_percent(100)  # Turn on pin 5
    print("Pin 5 ON")
    time.sleep(2)  # Wait for 2 seconds
    
    pwm5.pulse_width_percent(0)  # Turn off pin 5
    pwm6.pulse_width_percent(100)  # Turn on pin 6
    print("Pin 6 ON")
    time.sleep(2)  # Wait for 2 seconds
    
    pwm6.pulse_width_percent(0)  # Turn off pin 6

# Run the test
try:
    while True:
        test_leds()

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    # Reset PWM settings (if needed)
    pwm4.pulse_width_percent(0)
    pwm5.pulse_width_percent(0)
    pwm6.pulse_width_percent(0)
    print("PWM reset completed.")
