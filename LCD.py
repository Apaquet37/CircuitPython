import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.lcd import CursorMode
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

counter = 0

button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP

switch = DigitalInOut(board.D8)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

lcd.set_cursor_pos(1,0)
lcd.print("SwitchState:")

while True:
    if not button.value and oldButton:
        print("pressed!")
        lcd.set_cursor_pos(0,0)
        lcd.print("Presses:   ")
        lcd.print(str(counter))
        lcd.print("  ")
        #time.sleep(.05)
        if switch.value:
            lcd.set_cursor_pos(1,0)
            lcd.print("SwitchState:DOWN")
            print("switch")
            counter = counter - 1
            lcd.set_cursor_pos(0,11)
            lcd.print(str(counter))
            lcd.print("  ")
            time.sleep(.05)
        else:
            lcd.set_cursor_pos(1,0)
            lcd.print("SwitchState:UP  ")
            counter = counter + 1
            lcd.set_cursor_pos(0,11)
            lcd.print(str(counter))
            lcd.print("  ")
            time.sleep(.05)
    oldButton = button.value