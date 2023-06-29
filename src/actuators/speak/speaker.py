from abc import abstractmethod, ABC
from actuators.actuator import Acutator

class Speaker(Acutator, ABC):

    def actuate(self, message: str):
        self.speak(message)

    @abstractmethod
    def speak(self, message: str):
        pass
