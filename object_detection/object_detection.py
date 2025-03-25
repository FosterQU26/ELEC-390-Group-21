# For your consideration as the most abstracted code ever written

import tflite_runtime.interpreter as tflite
from pycoral.adapters import common, detect
from pycoral.adapters import classify
from pycoral.utils import edgetpu

import cv2
import numpy as np

interpreter = tflite.Interpreter(
    
    "/home/group21/ELEC-390-Group-21/object_detection/best_int8.tflite"
    
)

interpreter.allocate_tensors()

_input = interpreter.get_input_details()
_output = interpreter.get_output_details()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error loading video")
    exit()
    
else:
    
    print("Camera successfully connected")
    
while True:
    
    ret, frame = cap.read()
    if not ret:
        
        print("Failed to grab frame")
        break
    
    frame_re = cv2.resize(frame, common.input_size(interpreter))
    
    common.set_input(interpreter, frame_re)
    interpreter.invoke()
    output_details = interpreter.get_output_details()
    print(output_details)
     
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()




