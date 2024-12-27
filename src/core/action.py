from abc import ABC, abstractmethod

class Action(ABC):
    """
    Interface for actions.
    """
    @abstractmethod
    def execute(self, agent):
        """
        Method to execute the action.

        Parameters
        ----------
        agent : Agent
        """
        pass