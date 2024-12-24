from abc import ABC, abstractmethod
from enum import Enum
from core.events.interfaces.event_handler import EventHandler

class EventType(Enum):
    BLOCK_HIT = "BLOCK_HIT"
    CHAT_POST = "CHAT_POST"


class Event(ABC):
    """
    Interface for events
    """
    @abstractmethod
    def get_type(self):
        """
        Returns the type of the event.
        Returns
        -------
        EventType
        """
        pass

    @abstractmethod
    def get_entity_id(self):
        """
        Returns the entity id of the event.
        Returns
        -------
        int
        """
        pass

    @abstractmethod
    def accept(self, handler: EventHandler):
        """
        Method to accept a handler that process an event.

        Parameters
        ----------
        handler : EventHandler
        """
        pass