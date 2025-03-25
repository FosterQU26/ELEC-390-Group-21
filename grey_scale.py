from picarx import Picarx
from speed import Speed

px = Picarx()
car = Speed(px)

def adjust_direction():
    car.set_speed(10)
    """Adjust the car's direction based on grayscale sensor values."""
    sensor_values = px.get_grayscale_data()

    left_sensor = sensor_values[0]
    right_sensor = sensor_values[2]

    if left_sensor > 200 and right_sensor > 200:
        print("Both sensors detected high value! Stopping.")
        car.set_speed(0)
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

while adjust_direction():
    pass