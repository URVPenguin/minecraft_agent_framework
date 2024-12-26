from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, agent, args, kwargs):
        pass