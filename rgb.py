import pulseio
import time

class RGB:
    def __init__(self, r, g, b):
        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0)
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)
    def red(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 2**16-1
    def cyan(self):
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
    def rainbow(self):
        self.pwm_r.duty_cycle= 0
        self.pwm_g.duty_cycle= 2**16-1
        self.pwm_b.duty_cycle = 2**16-1
        for val in range(0,2**16-1, 64):
            self.pwm_r.duty_cycle= val
            self.pwm_g.duty_cycle= 2**16-1-val
            self.pwm_b.duty_cycle = 2**16-1
            time.sleep(0.01)
        for val in range(0,2**16-1, 64):
            self.pwm_r.duty_cycle= 2**16-1
            self.pwm_g.duty_cycle= val
            self.pwm_b.duty_cycle = 2**16-1-val
            time.sleep(0.01)
        for val in range(0,2**16-1, 64):
             self.pwm_r.duty_cycle= 2**16-1-val
             self.pwm_g.duty_cycle= 2**16-1
             self.pwm_b.duty_cycle = val
             time.sleep(0.01)
# cyan -- (0,255,255)
# magenta -- (180,0,180)
# red -- (255,0,0)
# green -- (0,255,0)
# yellow -- (255,150,0)
# blue -- (0,255,0)