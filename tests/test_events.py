import pytest

from core.events.block_event_adapter import BlockEventAdapter
from core.events.chat_event_adapter import ChatEventAdapter
from core.events.event_dispatcher import EventDispatcher
from core.events.interfaces.event import EventType
from core.events.interfaces.event_handler import EventHandler
from core.mcpi.event import BlockEvent, ChatEvent


class BlockEventHandler(EventHandler):
    def handle_block_event(self, event):
        print(f"BlockEventHandler: Bloque golpeado en posición {event.pos}, por entidad {event.entityId}")

    def handle_chat_event(self, event):
        # No hace nada con eventos de chat
        pass

class ChatEventHandler(EventHandler):
    def handle_block_event(self, event):
        # No hace nada con eventos de bloques
        pass

    def handle_chat_event(self, event):
        print(f"ChatEventHandler: Entidad {event.entityId} dijo '{event.message}'")

def test_event_dispatcher_singleton():
    dispatcher1 = EventDispatcher()
    dispatcher2 = EventDispatcher()

    assert dispatcher1 is dispatcher2

def test_event_adapters():
    block_event = BlockEventAdapter(BlockEvent(10, 64, -5, 1, 2, 2))
    assert block_event.get_type() == EventType.BLOCK_HIT
    assert block_event.get_entity_id() == 2

    chat_event = ChatEventAdapter(ChatEvent.Post(2, "Hello World"))
    assert chat_event.get_type() == EventType.CHAT_POST
    assert chat_event.get_entity_id() == 2

def test_block_event_handling(mocker):
    dispatcher = EventDispatcher()
    block_handler = BlockEventHandler()
    dispatcher.register(block_handler)
    mock_handle = mocker.patch.object(block_handler, 'handle_block_event')
    block_event = BlockEvent(10, 64, -5, 1, 2, 2)
    event = BlockEventAdapter(block_event)
    dispatcher.dispatch(event)
    mock_handle.assert_called_once_with(block_event)

def test_chat_event_handling(mocker):
    dispatcher = EventDispatcher()

    chat_handler = ChatEventHandler()
    dispatcher.register(chat_handler)

    mock_handle = mocker.patch.object(chat_handler, 'handle_chat_event')

    chat_event = ChatEvent.Post(2, "Hello World")
    event = ChatEventAdapter(chat_event)
    dispatcher.dispatch(event)
    mock_handle.assert_called_once_with(chat_event)