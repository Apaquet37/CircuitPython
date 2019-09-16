import time

import board
import pulseio

# PWM (fading) LEDs are connected on D0 (PWM not avail on D1)
pwm_leds = board.D0
pwm = pulseio.PWMOut(pwm_leds, frequency=1000, duty_cycle=0)


brightness = 0  # how bright the LED is
fade_amount = 1285  # 2% steping of 2^16


while True:

    # And send to LED as PWM level
    pwm.duty_cycle = brightness

    # change the brightness for next time through the loop:
    brightness = brightness + fade_amount

    print(brightness)

    # reverse the direction of the fading at the ends of the fade:
    if brightness <= 0:
        fade_amount = -fade_amount

    elif brightness >= 65535:
        fade_amount = -fade_amount


    # wait for 15 ms to see the dimming effect
    time.sleep(.015)
