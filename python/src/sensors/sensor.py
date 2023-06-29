from abc import abstractmethod, ABC


class Sensor(ABC):

    @abstractmethod
    def sense(self) -> object:
        return ""
    