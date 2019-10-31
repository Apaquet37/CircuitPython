import board  #pylint: disable-msg=import-error
import time
import digitalio  #pylint: disable-msg=import-error
import random  #random needs to be imported to allow for random choosing of numbers out of a given set

class FancyLED:
    def __init__(self,pin1,pin2,pin3): #defining the led objects with three pins, these pins are three separate leds
        self.pin1 = digitalio.DigitalInOut(pin1) #these are digital pins rather than pwm because they just need to turn on/off
        self.pin1.direction = digitalio.Direction.OUTPUT #leds are outputs
        self.pin2 = digitalio.DigitalInOut(pin2)
        self.pin2.direction = digitalio.Direction.OUTPUT
        self.pin3 = digitalio.DigitalInOut(pin3)
        self.pin3.direction = digitalio.Direction.OUTPUT
    def alternate(self): #My first function is alternate, which turns on the first and third leds, then the second led
                         #This only gets called for the first set of leds
        self.pin1.value = True #1st led on
        self.pin2.value = False #2nd led off
        self.pin3.value = True #3rd led on
        time.sleep(1)
        self.pin1.value = False #1st led off
        self.pin2.value = True #2nd led on
        self.pin3.value = False #3rd led off
        time.sleep(1)
        self.pin2.value = False #2nd led off
    def blink(self): #blink turns three leds on and then turns them off
        self.pin1.value = True #4th led on
        self.pin2.value = True #5th led on
        self.pin3.value = True #6th led on
        time.sleep(1)
        self.pin1.value = False #4th led off
        self.pin2.value = False #5th led off
        self.pin3.value = False #6th led off
        time.sleep(1)
    def chase(self): #the three leds in the first set turn on and then off in order
        self.pin1.value = True #1st on
        self.pin2.value = False #2nd off
        self.pin3.value = False #3rd off
        time.sleep(.5)
        self.pin1.value = False #1st off
        self.pin2.value = True #2nd on
        self.pin3.value = False #3rd off
        time.sleep(.5)
        self.pin1.value = False #1st off
        self.pin2.value = False #2nd off
        self.pin3.value = True #3rd on
        time.sleep(.5)
        self.pin3.value = False #3rd off so that things don't get too confusing
    
    def sparkle(self):
        for whatever in range(0,50):  #I want it to randomly flash 50 different times really fast
            print(whatever) #you can't have an unused variable, so "whatever" is printed in this otherwise useless line
            print("loop, n=")
            n= random.randint(0,3) #It randomly chooses a number from 0-3 and then I tell it what to do for each of the numbers
            print (n)
            print("\n")
            if n==0: #when n is zero all the leds in the second set turn on
                self.pin1.value = True
                self.pin2.value = True
                self.pin3.value = True
            if n==1: #for n = 1-3, one of the leds turns on
                self.pin1.value = False
                self.pin2.value = False
                self.pin3.value = True #6th led on
            if n==2:
                self.pin1.value = True #4th led on
                self.pin2.value = False
                self.pin3.value = False
            if n==3:
                self.pin1.value = False
                self.pin2.value = True #5th led on
                self.pin3.value = False
            time.sleep(.05) 
            # If you don't turn them all off at the end of each command it gets really confusing. 
            self.pin1.value = False
            self.pin2.value = False
            self.pin3.value = False  
