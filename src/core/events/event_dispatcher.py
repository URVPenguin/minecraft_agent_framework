from core.di.decorators.dependency import dependency
from core.events.interfaces.event import Event
from core.events.interfaces.event_handler import EventHandler

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
            self.handlers = []

    def register(self, handler: EventHandler):
        """
        Register an event handler with this dispatcher.

        Parameters
        ----------
        handler: EventHandler
        """
        self.handlers.append(handler)

    def dispatch(self, event: Event):
        """
        Dispatch an event in broadcast.

        Parameters
        ----------
        event: Event
        """
        for handler in self.handlers:
            event.accept(handler)
