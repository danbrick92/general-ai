from abc import abstractmethod, ABC


class Task(ABC):

    def __init__(self, actuators: list, sensors: list) -> None:
        self.actuators = actuators
        self.sensors = sensors

    @abstractmethod
    def perform_task(self):
        pass
    