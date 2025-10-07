# Blink the board led with 1 second interval, shorter code

import machine
import utime # specific to MicroPython, optimized for microcontroller use.

led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.toggle()
    utime.sleep(1)
