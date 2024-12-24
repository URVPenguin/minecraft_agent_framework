from core.di.decorators.dependency import dependency
from core.events.interfaces.event import Event
from core.events.interfaces.event_handler import EventHandler

@dependency
class EventDispatcher:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "handlers"):
            self.handlers = []

    def register(self, handler: EventHandler):
        self.handlers.append(handler)

    def dispatch(self, event: Event):
        for handler in self.handlers:
            event.accept(handler)
