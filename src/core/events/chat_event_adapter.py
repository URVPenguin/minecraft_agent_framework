from core.events.interfaces.event import Event, EventType
from core.events.interfaces.event_handler import EventHandler


class ChatEventAdapter(Event):

    def __init__(self, minecraft_event):
        super().__init__()
        self.minecraft_event = minecraft_event

    def get_type(self):
        return EventType.CHAT_POST

    def get_entity_id(self):
        return self.minecraft_event.entityId

    def accept(self, handler: EventHandler):
        handler.handle_chat_event(self.minecraft_event)
