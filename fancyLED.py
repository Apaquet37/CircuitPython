import board  #pylint: disable-msg=import-error
import time
import digitalio  #pylint: disable-msg=import-error

class FancyLED:
    def __init__(self,pin1,pin2,pin3):
        self.pin1 = digitalio.DigitalInOut(pin1)
        self.pin1.direction = digitalio.Direction.OUTPUT
        self.pin2 = digitalio.DigitalInOut(pin2)
        self.pin2.direction = digitalio.Direction.OUTPUT
        self.pin3 = digitalio.DigitalInOut(pin3)
        self.pin3.direction = digitalio.Direction.OUTPUT
    def alternate(self):
        self.pin1 = True
        self.pin2 = False
        self.pin3 = True
        time.sleep(1)
        self.pin1 = False
        self.pin2 = True
        self.pin3 = False
    def blink(self):
        self.pin1 = True
        self.pin2 = True
        self.pin3 = True
        time.sleep(1)
    def chase(self):
        self.pin1 = True
        self.pin2 = True
        self.pin3 = True
        time.sleep(1)
    def sparkle(self):
        self.pin1 = True
        self.pin2 = True
        self.pin3 = True
        time.sleep(1)        