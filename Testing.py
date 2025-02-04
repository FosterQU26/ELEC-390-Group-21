#Testing Scripts in Python for the project

from picarx import Picarx
import time

if __name__ == "__main__" :
    try:
        #initilize a Picarx object
        px = Picarx()
        #Motor Test
        px.forward(10)      #Move forward
        time.sleep(2.5)
        px.backward(10)     #Move Backward
        time.sleep(2.5)
        px.stop()
        #Test Cervos
        for angle in range(0, 35):
            px.set_dir_servo_angle(angle)
            px.set_cam_pan_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35, -1):
            px.set_dir_servo_angle(angle)
            px.set_cam_pan_angle(angle)
            time.sleep(0.01)
        for angle in range(-35, 0):
            px.set_dir_servo_angle(angle)
            px.set_cam_pan_angle(angle)
            time.sleep(0.01)
        #Turn Camera up Down
        for angle in range(0, 35):
            px.set_cam_tilt_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35,-1):
            px.set_cam_tilt_angle(angle)
            time.sleep(0.01)        
        for angle in range(-35, 0):
            px.set_cam_tilt_angle(angle)
            time.sleep(0.01)

    finally:
        px.stop()
        time.sleep(0.2)    
