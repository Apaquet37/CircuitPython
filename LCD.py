import time
import board
import busio #A library necessary for LCD screens
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD #Getting the LCD from the lcd library
from lcd.lcd import CursorMode #Lets you use cursor mode with the lcd
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface #Importing the LCD backpack
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16) #LCD setup

counter = 0 #The counter starts at zero

button = DigitalInOut(board.D2) #My button is connected to digital pin 2
button.direction = Direction.INPUT #The button is collecting information, therfore it is an input
button.pull = Pull.UP 

switch = DigitalInOut(board.D8) #My switch is connected to digital pin 8
switch.direction = Direction.INPUT #The switch is also an input
switch.pull = Pull.UP

lcd.set_cursor_pos(1,0) #Printing SwitchState: in the first spot of the second row
lcd.print("SwitchState:")

while True:
    if not button.value and oldButton:#If the button is being pressed, and it has been lifted since the last time it was pressed
        print("pressed!") #The serial monitor will let me know when the button is pressed
        lcd.set_cursor_pos(0,0) #Starting in the very first position
        lcd.print("Presses:   ") #The lcd screen will show the number of times the button has been pressed
        lcd.print(str(counter)) #Printing the number of presses to the lcd
        lcd.print("  ") #Formatting to make the lcd printing and spacing look right
        #time.sleep(.05)
        if switch.value: #If the switch is off
            lcd.set_cursor_pos(1,0)
            lcd.print("SwitchState:DOWN") #Printing to the lcd the state of the switch
            print("switch") #Let me know on the serial monitor that the switch has been flipped
            counter = counter - 1 #Count down
            lcd.set_cursor_pos(0,11) 
            lcd.print(str(counter))
            lcd.print("  ")
            time.sleep(.05)
        else: #If the switch is on
            lcd.set_cursor_pos(1,0)
            lcd.print("SwitchState:UP  ") #Printing to the lcd the state of the switch
            counter = counter + 1 #Count up
            lcd.set_cursor_pos(0,11)
            lcd.print(str(counter))
            lcd.print("  ")
            time.sleep(.05)
    oldButton = button.value #This code makes it so that if you hold down the button it only counts up one, it needs the button to be 
                             #unpressed before it can count again
