import pulseio #this code uses pwm so you need the pulseio library
import time

class RGB:
    def __init__(self, r, g, b): #setting up the object with three pins, corresponding to the ones in the main code
                                 #this works to set up both of the leds
    #these are all pwm so that they can fade and not just turn on and off   
    self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0) #this is for the red legs on the two leds
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0) #this is for the green legs on the two leds
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0) #this is for the blue legs on the two leds
    def red(self): #this is my red function, it turns red all the way up and green and blue to zero
        self.pwm_r.duty_cycle = 0 #you set a pin to zero if you want it to turn on
        self.pwm_g.duty_cycle = 2**16-1 #2**16-1 is how you make sure a pin is all the way off
        self.pwm_b.duty_cycle = 2**16-1
    def cyan(self): #there is a function for each of the colors
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 0
    def magenta(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0
    def green(self):
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 2**16-1
    def yellow(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 2**16-1
    def blue(self):
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0
    def rainbow(self): #This function cycles through the colors on both leds
        self.pwm_r.duty_cycle= 0 #starting at red
        self.pwm_g.duty_cycle= 2**16-1
        self.pwm_b.duty_cycle = 2**16-1
        for val in range(0,2**16-1, 64): #When value is between 0 and 2**16-1, val should go up by 64
            self.pwm_r.duty_cycle= val #Slowly fading out the red (val is approaching 2**16-1 so red is going away)
            self.pwm_g.duty_cycle= 2**16-1-val #and fading in the green, so that this fades from red, through yellow, to green
            self.pwm_b.duty_cycle = 2**16-1 #Blue stays off
            time.sleep(0.01)
        for val in range(0,2**16-1, 64):
            self.pwm_r.duty_cycle= 2**16-1 #No red
            self.pwm_g.duty_cycle= val #Green is slowly fading away,
            self.pwm_b.duty_cycle = 2**16-1-val #while blue takes its place
            time.sleep(0.01)
        for val in range(0,2**16-1, 64):
             self.pwm_r.duty_cycle= 2**16-1-val #red is increasing
             self.pwm_g.duty_cycle= 2**16-1 #No green
             self.pwm_b.duty_cycle = val #blue is decreasing, this goes from blue, through purple, back to red
             time.sleep(0.01)
# cyan -- (0,255,255)
# magenta -- (180,0,180)
# red -- (255,0,0)
# green -- (0,255,0)
# yellow -- (255,150,0)
# blue -- (0,255,0)
