import board
import time
import digitalio

class FancyLED:
    def __init__(self,pin1,pin2,pin3):
        self.pin1 = digitalio.DigitalInOut(pin1)
        self.pin1.direction = digitalio.Direction.OUTPUT
        self.pin2 = digitalio.DigitalInOut(pin2)
        self.pin2.direction = digitalio.Direction.OUTPUT
        self.pin3 = digitalio.DigitalInOut(pin3)
        self.pin3.direction = digitalio.Direction.OUTPUT
    def alternate(self):

    def blink(self):

    def chase(self):

    def sparkle(self):
        