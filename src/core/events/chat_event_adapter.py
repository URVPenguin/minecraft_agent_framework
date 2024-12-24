from core.events.interfaces.event import Event, EventType
from core.events.interfaces.event_handler import EventHandler


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

    def accept(self, handler: EventHandler):
        """
        Method for calling event handler of the client

        Parameters
        ----------
        handler: EventHandler
        """
        handler.handle_chat_event(self.minecraft_event)
