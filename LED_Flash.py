from robot_hat import Pin
from time import sleep

pin = Pin("D1")                      # create a Pin object from a digital pin

while (1):
  print("Off")
  pin.value(0)                         # set the digital pin to low level
  sleep(0.5)
  pin.value(1)                         # set the digital pin to low level
  print("On")
  sleep(0.5)
