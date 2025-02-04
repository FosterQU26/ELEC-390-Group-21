from robot_hat import Pin

pin = Pin("D0")                      # create a Pin object from a digital pin

while (1)
  pin.value(0)                         # set the digital pin to low level
  wait(0.5)
  pin.value(1)                         # set the digital pin to low level
