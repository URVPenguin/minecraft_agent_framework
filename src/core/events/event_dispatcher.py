from core.di.decorators.dependency import dependency
from core.events.interfaces.event import Event
from core.events.interfaces.event_handler import EventHandler
from core.agent import Agent

@dependency
class EventDispatcher:
    """
    This class is responsible for dispatching events to specific handlers.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "handlers"):
            self.handlers = {}

    def register(self, handler: EventHandler, agent):
        """
        Register an event handler with this dispatcher.

        Parameters
        ----------
        agent : Agent
        handler: EventHandler
        """
        self.handlers[agent] = handler

    def dispatch(self, event: Event):
        """
        Dispatch an event in broadcast.

        Parameters
        ----------
        event: Event
        """
        for agent, handler in self.handlers.items():
            event.accept(handler, agent)
