# Blink the board led with 1 second interval

import machine # used for accessing hardware components of a microcontroller.
import time # provides time-related functions.


#configure internal LED Pin as output pin and create led object for Pin class:

led = machine.Pin('LED', machine.Pin.OUT)

# Never ending loop

while True:
  led.value(True) # turn on the LED
  time.sleep(1) # wait for one second
  led.value(False) # turn off the LED
  time.sleep(1) # wait for one second
