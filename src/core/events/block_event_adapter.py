from core.events.interfaces.event import Event, EventType
from core.events.interfaces.event_handler import EventHandler
from core.agent import Agent

class Vec:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class BlockEventAdapter(Event):
    """
    Adapter object for block events.
    """
    def __init__(self, minecraft_event):
        super().__init__()
        self._minecraft_event = minecraft_event

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
        return self._minecraft_event.entityId

    def get_data(self):
        """
        Getter for entity pos
        Returns
        -------
        Vec
        """
        x, y, z = self._minecraft_event.pos
        return Vec(x, y, z)

    def accept(self, handler: EventHandler, agent: Agent):
        """
        Method for calling event handler of the client
        Parameters
        ----------
        agent: Agent
        handler: EventHandler

        """
        handler.handle_block_event(self, agent)

