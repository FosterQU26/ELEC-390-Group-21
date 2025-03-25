from picarx import Picarx
from time import sleep
import readchar

from robot_hat import PWM

# Create PWM objects for each pin
pwm4 = PWM('P4')  # Pin 4
pwm5 = PWM('P5')  # Pin 5
pwm6 = PWM('P6')  # Pin 6

# Set frequency and prescaler for each PWM pin (example values)
freq = 1000  # Frequency in Hz
prescaler = 1  # Prescaler value (0-255, typically for adjusting the frequency)
period = 1000  # Period (this can vary depending on your needs)
pulse_width = 500  # Pulse width in microseconds (for on-time duration)
pulse_width_percent = 100  # Duty cycle in percentage (0-100)

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

if __name__ == "__main__":
    try:
        pan_angle = 0
        tilt_angle = 0
        px = Picarx()
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsadkl'):
                if 'w' == key:
                    pwm4.pulse_width_percent(0)
                    px.set_dir_servo_angle(0)
                    px.forward(80)
                elif 's' == key:
                    px.set_dir_servo_angle(0)
                    px.backward(80)
                elif 'a' == key:
                    px.set_dir_servo_angle(-35)
                    px.forward(80)
                elif 'd' == key:
                    px.set_dir_servo_angle(35)
                    px.forward(80)
                elif 'k' == key:
                    print("Signal Left")
                    pwm5.pulse_width_percent(100)  # Turn on pin 5
                    print("Pin 5 ON")
                elif 'l' == key:
                    print("Signal Right")
                    pwm6.pulse_width_percent(100)  # Turn on pin 6
                    print("Pin 6 ON")

                sleep(1)
                px.forward(0)
                pwm4.pulse_width_percent(100)
                pwm5.pulse_width_percent(0)
                pwm6.pulse_width_percent(0)

            elif key == readchar.key.CTRL_C:
                print("\n Quit")
                break

    finally:
        px.set_dir_servo_angle(0)
        px.stop()
        sleep(.2)
