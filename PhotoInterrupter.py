import board
import time
from digitalio import DigitalInOut, Direction, Pull

photo = DigitalInOut(board.D13)
photo.direction = Direction.INPUT
photo.pull = Pull.UP
counter = 0
initial = time.monotonic() #Time monotonic allows you to count how much time has passed since the sketch ran, initial is a variable I'm
                           #making to use later on

while True:
    now = time.monotonic() #This variable updates everytime the while true loop runs, making it the current time
    if now - initial > 4: #If the current time minus the time this loop last ran is more than 4, run again
                          #Basically just making the loop run every 4 seconds
        print("The number of interrupts is ", counter) #Printing the number of interuppts to the serial monitor every four seconds
        initial = now #Initial gets set to the current time at the end of very loop where you print

    if not photo.value: #This loop goes when the photo interrupter hasn't been interrupted
        time.sleep(.25)

    else: #This is what happens when the photo interrupter is triggered
        counter = counter + 1 #Adding one to the counter so that an accurate number of interrupts can be printed
        time.sleep(.25)
