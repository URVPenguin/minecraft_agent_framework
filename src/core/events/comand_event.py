from core.events.interfaces.event import Event, EventType
from core.events.interfaces.event_handler import EventHandler
from core.agent import Agent

class CommandEvent(Event):
    """
    Event class to notify commands
    """
    def __init__(self, entity_id, command, args, kwargs):
        super().__init__()
        self.command = command
        self.args = args
        self.kwargs = kwargs
        self.entity_id = entity_id

    def get_type(self):
        """
        Returns the type of the event.
        Returns
        -------
        EventType
        """
        return EventType.COMMAND

    def get_entity_id(self):
        """
        Returns the entity ID of the event.
        Returns
        -------
        int
        """
        return self.entity_id

    def get_data(self):
        """
        Returns command and command args.
        Returns
        -------
        dict
        """
        return {"command": self.command, "args": self.args, "kwargs": self.kwargs}

    def accept(self, handler: EventHandler, agent: Agent):
        """
        Method for calling event handler of the client

        Parameters
        ----------
        agent: Agent
        handler: EventHandler
        """
        handler.handle_command_event(self, agent)
