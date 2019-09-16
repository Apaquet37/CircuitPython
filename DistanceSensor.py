import board
import time
import digitalio
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D9)
import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3
r = 255
g = 0
b = 0

while True:
    try:
        distance = int(sonar.distance)
        print((sonar.distance))
        time.sleep(.1)
        print(r,g,b)
        led.fill((r, g, b))
    except RuntimeError:
        #print("Retrying!")
        pass
    if distance <= 5:
        r = 255
        b = 0
        g = 0
    if distance <= 20 and distance > 5:
        r = 255 - (17*distance)
        b = 0 + (17*distance)
        g = 0
    if distance > 20:
        r = 0
        b = 255 - (17*(distance-20))
        g = 0 + (17*(distance-20))
    if r < 0:
        r = 0
    if b < 0:
        b = 0
    if g > 255:
        g = 255
    if b > 255:
        b = 255