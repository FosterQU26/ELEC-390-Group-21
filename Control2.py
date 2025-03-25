from picarx import Picarx
from time import sleep
import readchar

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
                elif 'l' == key:
                    print("Signal Right")


                sleep(0.5)
                px.forward(0)

            elif key == readchar.key.CTRL_C:
                print("\n Quit")
                break

    finally:
        px.set_dir_servo_angle(0)
        px.stop()
        sleep(.2)
