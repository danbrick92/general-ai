# Imports
import RPi.GPIO as GPIO
import logging
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


class RGBLed:
    
    colors = {
        'red': (1,0,0),
        'green': (0,1,0),
        'blue': (0,0,1),
        'yellow': (1,1,0),
        'purple': (1,0,1),
        'teal': (0,1,1),
        'white': (1,1,1),
        'off': (0,0,0)
    }
    
    def __init__(self, r_pin=11, g_pin=13, b_pin=15):
        self.r_pin = r_pin
        self.g_pin = g_pin
        self.b_pin = b_pin
        GPIO.setup(r_pin, GPIO.OUT)
        GPIO.setup(g_pin, GPIO.OUT)
        GPIO.setup(b_pin, GPIO.OUT)
        self.reset()
        
    def set_color(self, color: str):
        color_tuple = self.colors[color]
        logging.debug(f"Setting RGB LED color: {color} with tuple {color_tuple}")
        
        # HIGH/LOW flipped so using not
        GPIO.output(self.r_pin, not color_tuple[0])
        GPIO.output(self.g_pin, not color_tuple[1])
        GPIO.output(self.b_pin, not color_tuple[2])
        
    def reset(self):
        self.set_color(color='off')
        
    def set_state(self, state: str):
        if state == 'await_key':
            self.set_color('blue')
        elif state == 'busy':
            self.set_color('yellow')
        elif state == 'recording':
            self.set_color('green')
        elif state == 'error':
            self.set_color('red')
        elif state == 'chatgpt_busy':
            self.set_color('purple')
