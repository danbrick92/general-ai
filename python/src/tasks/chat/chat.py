from tasks.task import Task
from abc import ABC, abstractmethod
from sensors.listen.listener import Listener
from actuators.speak.speaker import Speaker


class Chat(Task, ABC):

    def __init__(self, actuators: list, sensors: list):
        super().__init__(actuators, sensors)

        # Ensure we have sensor and actuator for listening
        assert len(self.sensors) == 1
        assert len(self.actuators) == 1

        # Set sensor and actuator
        sensor = self.sensors[0]
        actuator = self.actuators[0]

        # Ensure they are of Listening and Speaking type
        assert isinstance(sensor, Listener)
        assert isinstance(actuator, Speaker)

        self.listener = sensor
        self.speaker = actuator

    def perform_task(self):
        self.chat()

    @abstractmethod
    def chat(self):
        pass
