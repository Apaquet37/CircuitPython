import time #this allows me to use commands that use time

import board #you need this for any code to work, it allows your code to see board specific details
import pulseio

# PWM (fading) LEDs are connected on D0 (PWM not avail on D1)
pwm_leds = board.D0 #My LED is connected to digital pin 0
pwm = pulseio.PWMOut(pwm_leds, frequency=1000, duty_cycle=0) #This makes my LED and output so that it can receive commands from the code


brightness = 0  # how bright the LED is
fade_amount = 1285  # 2% stepping of 2^16


while True:

    # And send to LED as PWM level
    pwm.duty_cycle = brightness #The LED glows as bright as the brightness variable

    # change the brightness for next time through the loop:
    brightness = brightness + fade_amount

    print(brightness)

    # reverse the direction of the fading at the ends of the fade:
    # code to switch the direction to make sure that the brightness doesn't go out of range
    if brightness <= 0: 
        fade_amount = -fade_amount

    elif brightness >= 65535:
        fade_amount = -fade_amount


    # wait for 15 ms to see the dimming effect
    time.sleep(.015)
