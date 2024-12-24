from core.events.interfaces.event import Event, EventType
from core.events.interfaces.event_handler import EventHandler


class BlockEventAdapter(Event):
    """
    Adapter object for block events.
    """
    def __init__(self, minecraft_event):
        super().__init__()
        self.minecraft_event = minecraft_event

    def get_type(self):
        """
        Getter for block event type
        Returns
        -------
        EventType
        """
        return EventType.BLOCK_HIT

    def get_entity_id(self):
        """
        Getter for entity id
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
        handler.handle_block_event(self.minecraft_event)

