from actuators.speak.speaker import Speaker
import pyttsx3
import logging


class PyTTSX3(Speaker):

    def __init__(self):
        logging.debug("Setting up PyTSX3...")
        super().__init__()
        self.engine = pyttsx3.init()

    def speak(self, message: str):
        logging.info(f"Saying: {message}...")
        print(message)
        self.engine.say(message)
        self.engine.runAndWait()

    def set_male_voice(self):
        logging.info(f"Setting voice to male...")
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def set_female_voice(self):
        logging.info(f"Setting voice to female...")
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
