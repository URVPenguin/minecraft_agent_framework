from core.events.interfaces.event import Event, EventType
from core.events.interfaces.event_handler import EventHandler
from core.agent import Agent

class ChatEventAdapter(Event):
    """
    Adapter object for chat events.
    """
    def __init__(self, minecraft_event):
        super().__init__()
        self.minecraft_event = minecraft_event

    def get_type(self):
        """
        Returns the type of the event.
        Returns
        -------
        EventType
        """
        return EventType.CHAT_POST

    def get_entity_id(self):
        """
        Returns the entity ID of the event.
        Returns
        -------
        int
        """
        return self.minecraft_event.entityId

    def get_data(self):
        """
        Returns the message.
        Returns
        -------
        string
        """
        return self.minecraft_event.message

    def accept(self, handler: EventHandler, agent: Agent):
        """
        Method for calling event handler of the client

        Parameters
        ----------
        agent: Agent
        handler: EventHandler
        """
        handler.handle_chat_event(self, agent)
