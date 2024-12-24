from abc import ABC, abstractmethod

class EventHandler(ABC):
    """
    Interface for event handlers.
    """
    @abstractmethod
    def handle_block_event(self, event):
        """
        Manage a BlockEventAdapter type

        Parameters
        ----------
        event: BlockEventAdapter
        """
        pass

    @abstractmethod
    def handle_chat_event(self, event):
        """
        Manage a ChatEventAdapter type

        Parameters
        ----------
        event: ChatEventAdapter
        """
        pass