# Embedded programming exercise 1
# Tehtävänanto: printing numbers from 0-9

import time
time.sleep(0.1) # Wait for USB to become ready

print("Ready to go!")

print("Loop starting")

# käytetään for loop-rakennetta

for x in range(0, 10):
  print("Loop number: ", x)

print("Loop finished")