import board
import time
import digitalio
import adafruit_hcsr04 #This is the file we needed to add into our lib folder to make the sensor work
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D9) #Saying which pins the distance sensor is connected to
import neopixel #Library for the onboard neopixel LED
led = neopixel.NeoPixel(board.NEOPIXEL, 1) #Setting up the neopixel
led.brightness = 0.3 #Setting the correct brightness for the neopixel
r = 255 #Starting the LED at red
g = 0
b = 0

while True:
    try: #You have to put "try" so that the code doesn't just stop when the hcsr04 doesn't get a distance
        distance = int(sonar.distance) #A new variable named distance is used for all the led work so that even if we don't 
                                       #get a new distance in any give loop, the led will still work
        print((sonar.distance)) #Printing the distance every second
        time.sleep(.1)
        print(r,g,b) #Printing my color variables so I can make sure they're working right
        led.fill((r, g, b)) #Using my r, g, and b variables to light up the LED
    except RuntimeError: #If there is an error with the distance sensor, it just prints retrying and keeps going 
        #print("Retrying!")
        pass
    if distance <= 5: #When the distance is less than 5 the LED is red
        r = 255
        b = 0
        g = 0
    if distance <= 20 and distance > 5: #When the distance is between 5 and 20, the red goes down slowly as the blue goes up
        r = 255 - (17*distance)
        b = 0 + (17*distance)
        g = 0
    if distance > 20: #When the distance is greater than 20, the LED gradually fades from blue to green
        r = 0
        b = 255 - (17*(distance-20))
        g = 0 + (17*(distance-20))
    
    #Compensating for errors in my math so that the values for the LED never go out of range 
    if r < 0:
        r = 0
    if b < 0:
        b = 0
    if g > 255:
        g = 255
    if b > 255:
        b = 255
