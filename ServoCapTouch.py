import time
import board
import pulseio
import touchio
from adafruit_motor import servo

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)

angle = 90
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    if touch_A1.value:
        if angle <= 179:
            my_servo.angle = angle
            time.sleep(.03)
            angle = angle+1
    if touch_A2.value:
        if angle >= 1:
            my_servo.angle = angle
            time.sleep(.03)
            angle = angle-1

