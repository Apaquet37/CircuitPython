# CircuitPython
My CircuitPython assignments:
## LED Fade
In this assignment I learned how to code for an LED in circuitpython and then make the LED fade in and out. 
## Servo Capacitive Touch
This makes a servo move using capacitive touch. There are two wires just plugged into analog pins in the metro, and when either of them are touched, they are grounded. In this assignment, when one wire is touched the servo spins one way, and when the other is touched the servo turns the other way.
## LCD Screen
For this, an LCD screen displays the number of times a button has been pressed. In addition, there is a switch that will change the direction the counter is going if flipped. To make sure that the button only counted up one each press, even if it was held down, I had to add in an oldButtonState variable.
## Photo Interrupter
In this assignment I learned how to wire the new photo interrupters and how to code for them with circuitpython. In CircuitPython, a photo interrupter can be coded essentially the same as a button, making this assignment pretty easy. In addition, I learned about time monotonic which allowed me to calculate how long it had been since a loop had run, thus enabling me to have something run every four seconds without using time.sleep. When the photo interrupter is interrupted, it adds to a count, and that count prints every four seconds.
## Distance Sensor
Here I used an HCSR04 ultrasonic sensor to control the internal RGB LED on the metro. The assignment was to have the LED gradually change colors corresponding to the distance the sensor was reading. For most of the sensor code I was able to look at the HCSR04 library we were using to get information. The hardest part of this assignment was figuring out how to get the RGB LED spectrum working smoothly with the distance values.
## Hello VS Code
This was an introduction to Visual Studio (VS) Code. VS Code is similar to Mu, but a big advantage it has is built in git. You can add, commit, and push your changes with git, without leaving VS Code. In addition, when you edit your README in VS Code, you can open a preview on the side and see what it will look like.
## Fancy LED
Fancy LED was another assignment similar to rgb LED, where you are getting the hang of making classes. In this one, there were four methods, alternate, blink, chase, and sparkle. For alternate, I had two leds blink and then one led blink. For blink, I had all three leds turn on at once. In chase, I had the first, then the second, then the third leds turn on in turn. For sparkle, I had a random combination of the three leds turn on 50 times really fast.