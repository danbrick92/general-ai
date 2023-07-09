# Imports
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


class ClickButton:
    
    def __init__(self, pin=16):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
    def await_input(self) -> bool:
        while True:
            if GPIO.input(self.pin) == GPIO.HIGH:
                return True
        
    