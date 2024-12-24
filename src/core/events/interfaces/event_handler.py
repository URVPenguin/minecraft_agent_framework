from abc import ABC, abstractmethod

class EventHandler(ABC):
    """
    Interface for event handlers.
    """
    @abstractmethod
    def handle_block_event(self, event, agent):
        """
        Manage a BlockEventAdapter type

        Parameters
        ----------
        agent: Agent
        event: BlockEventAdapter
        """
        pass

    @abstractmethod
    def handle_chat_event(self, event, agent):
        """
        Manage a ChatEventAdapter type

        Parameters
        ----------
        agent: Agent
        event: ChatEventAdapter
        """
        pass