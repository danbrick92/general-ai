from actuators.speak.speaker import Speaker
import logging


class SystemOut(Speaker):

    def speak(self, message: str):
        logging.debug(f"Showing: {message}")
        print(message)
