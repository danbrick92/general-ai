from abc import abstractmethod, ABC
from sensors.sensor import Sensor


class Listener(Sensor, ABC):

    def sense(self) -> str:
        return self.listen()

    @abstractmethod
    def listen(self) -> str:
        pass
