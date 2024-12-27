from abc import ABC, abstractmethod

class Command(ABC):
    """
    Interface for commands
    """
    @abstractmethod
    def execute(self, agent, args, kwargs):
        """
        Executes the command

        Parameters
        ----------
        agent : Agent
        args
        kwargs
        """
        pass