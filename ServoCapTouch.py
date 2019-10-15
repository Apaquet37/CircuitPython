import time
import board
import pulseio # This module makes pwm objects work
import touchio # This is the module necessary to make capacitive touch work
from adafruit_motor import servo # Getting the servo library so its commands will work

touch_A1 = touchio.TouchIn(board.A1) #These are the two pins that I just have wires sticking out of
touch_A2 = touchio.TouchIn(board.A2) #When you touch either of the two wires, it grounds and you can make something happen

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50) #This is the setup for my servo, it's similar to that of an LED

angle = 90 # Starting the servo in the middle, not moving
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    if touch_A1.value: # If the first wire is touched
        if angle <= 179: # and the angle isn't too big
            my_servo.angle = angle 
            time.sleep(.03)
            angle = angle+1 # Move the servo one direction
    if touch_A2.value: # If the other wire is touched
        if angle >= 1: # and the angle isn't too small
            my_servo.angle = angle
            time.sleep(.03)
            angle = angle-1 # Move the servo the other direction

