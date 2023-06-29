from sensors.listen.listener import Listener
import logging


class SystemIn(Listener):

    prefix = "Type your message here: "

    def listen(self) -> str:
        logging.debug("Gathering input from user...")
        message = input(self.prefix)
        return message

    def set_prefix(self, prefix: str):
        logging.debug(f"Setting prefix as {prefix}")
        self.prefix = prefix
