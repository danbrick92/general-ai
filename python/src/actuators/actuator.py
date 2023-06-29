from abc import abstractmethod, ABC

class Acutator(ABC):

    @abstractmethod
    def actuate(self, data: object):
        pass
