from abc import ABC, abstractmethod
from enum import Enum
from core.events.interfaces.event_handler import EventHandler
from core.agent import Agent

class EventType(Enum):
    BLOCK_HIT = "BLOCK_HIT"
    CHAT_POST = "CHAT_POST"
    COMMAND = "COMMAND"

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
    def get_data(self):
        """
        Returns the event data.

        Returns
        -------
        Any
        """
        pass

    @abstractmethod
    def accept(self, handler: EventHandler, agent):
        """
        Method to accept a handler that process an event.

        Parameters
        ----------
        agent : Agent
        handler : EventHandler
        """
        pass