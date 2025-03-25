from picarx import Picarx
from robot_hat import PWM
from time import sleep
import readchar

px = Picarx()

# Create PWM objects for each pin
pwm4 = PWM('P4')  # Pin 4
pwm5 = PWM('P5')  # Pin 5
pwm6 = PWM('P6')  # Pin 6

# Set frequency and prescaler for each PWM pin (example values)
freq = 1000  # Frequency in Hz
prescaler = 1  # Prescaler value (0-255, typically for adjusting the frequency)
period = 1000  # Period (this can vary depending on your needs)
pulse_width = 500  # Pulse width in microseconds (for on-time duration)
pulse_width_percent = 0  # Duty cycle in percentage (0-100)

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

def signal_right ():
    pwm6.pulse_width_percent(100)
    sleep(0.20)
    pwm6.pulse_width_percent(0)
    sleep(0.20)
    pwm6.pulse_width_percent(100)
    sleep(0.20)
    pwm6.pulse_width_percent(0)
    sleep(0.20)
    pwm6.pulse_width_percent(100)
    sleep(0.20)
    pwm6.pulse_width_percent(0)
    
def signal_left ():
    pwm5.pulse_width_percent(100)
    sleep(0.20)
    pwm5.pulse_width_percent(0)
    sleep(0.20)
    pwm5.pulse_width_percent(100)
    sleep(0.20)
    pwm5.pulse_width_percent(0)
    sleep(0.20)
    pwm5.pulse_width_percent(100)
    sleep(0.20)
    pwm5.pulse_width_percent(0)

def drive():
    while adjust_direction():
        sleep(0.1)

def adjust_direction():
    px.forward(10)
    """Adjust the car's direction based on grayscale sensor values."""
    sensor_values = px.get_grayscale_data()

    left_sensor = sensor_values[0]
    center_sensor = sensor_values[1]
    right_sensor = sensor_values[2]

    if left_sensor > 200 and center_sensor > 200 and right_sensor > 200:
        print("Both sensors detected high value! Stopping.")
        px.forward(0)
        return False
    elif left_sensor > 200:
        print("Left sensor detected high value! Turning right.")
        px.set_dir_servo_angle(30)  # Adjust the angle as needed
        return True
    elif right_sensor > 200:
        print("Right sensor detected high value! Turning left.")
        px.set_dir_servo_angle(-30)  # Adjust the angle as needed
        return True
    else:
        px.set_dir_servo_angle(0)
        return True

print(px.get_grayscale_data())
sleep(2)
print("Showtime")
drive()
'''
while 1:
    key = readchar.readkey()
    key = key.lower()
    if key in ('wadkl'):
        if 'w' == key:
            drive()
        elif 'a' == key:
            px.set_dir_servo_angle(-35)
            px.forward(2)
        elif 'd' == key:
            px.set_dir_servo_angle(35)
            px.forward(2)
        elif 'k' == key:
            print("Signal Left")
            signal_left()
        elif 'l' == key:
            print("Signal Right")
            signal_right()
    elif key == 'q':
        break 
    sleep(1)  

pwm4.pulse_width_percent(0)
pwm5.pulse_width_percent(0)
pwm6.pulse_width_percent(0)
px.set_dir_servo_angle(0)
px.forward(0)
px.stop() 


print("Finished")


'''
