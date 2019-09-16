import board
import time
from digitalio import DigitalInOut, Direction, Pull

photo = DigitalInOut(board.D13)
photo.direction = Direction.INPUT
photo.pull = Pull.UP
counter = 0
initial = time.monotonic()

while True:
    now = time.monotonic()
    if now - initial > 4:
        print("The number of interrupts is ", counter)
        initial = now

    if not photo.value:
        time.sleep(.25)

    else:
        counter = counter + 1
        time.sleep(.25)