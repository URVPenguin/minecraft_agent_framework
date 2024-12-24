from unittest.mock import MagicMock

import pytest
from core.action import Action
from core.agent import Agent
from core.di.container import DependencyContainer
from core.events.block_event_adapter import BlockEventAdapter, Vec
from core.events.chat_event_adapter import ChatEventAdapter
from core.events.event_dispatcher import EventDispatcher
from core.events.interfaces.event import EventType, Event
from core.events.interfaces.event_handler import EventHandler
from core.mcpi.event import BlockEvent, ChatEvent
from core.services.minecraft_service import MinecraftService


class CustomEventHandler(EventHandler):
    def handle_block_event(self, event, agent):
        print(f"BlockEventHandler: Block hit in {event.get_data()}, by entity: {event.get_entity_id()}")

    def handle_chat_event(self, event, agent):
        print(f"ChatEventHandler: Entity: {event.get_entity_id()} says '{event.get_data()}'")

class PlaceBlockAction(Action):
    def execute(self, agent: Agent):
        print(f"{agent.name} action'")


@pytest.fixture
def mock_minecraft_service():
    mock_service = MagicMock(MinecraftService)
    mock_instance = MagicMock()

    mock_service.get_instance.return_value = mock_instance
    mock_instance.player.getTilePos.return_value = MagicMock(x=0, y=0, z=0)
    mock_instance.setBlock = MagicMock()
    mock_instance.postToChat = MagicMock()

    return mock_service, mock_instance

@pytest.fixture
def configure_dependencies(mock_minecraft_service):
    mock_service, _ = mock_minecraft_service
    DependencyContainer()._registrations = {}
    DependencyContainer().register(MinecraftService, mock_service)

def test_event_dispatcher_singleton():
    dispatcher1 = EventDispatcher()
    dispatcher2 = EventDispatcher()

    assert dispatcher1 is dispatcher2

def test_event_adapters():
    block_event = BlockEventAdapter(BlockEvent(10, 64, -5, 1, 2, 2))
    assert block_event.get_type() == EventType.BLOCK_HIT
    assert block_event.get_entity_id() == 2
    assert isinstance(block_event.get_data(), Vec)

    chat_event = ChatEventAdapter(ChatEvent.Post(2, "Hello World"))
    assert chat_event.get_type() == EventType.CHAT_POST
    assert chat_event.get_entity_id() == 2
    assert chat_event.get_data() == "Hello World"

def test_block_event_handling(mocker, mock_minecraft_service, configure_dependencies):
    dispatcher = EventDispatcher()
    handler = CustomEventHandler()
    agent =  Agent("Test", PlaceBlockAction(), handler)
    dispatcher.register(handler, agent)
    mock_handle = mocker.patch.object(handler, 'handle_block_event')
    block_event = BlockEvent(10, 64, -5, 1, 2, 2)
    event = BlockEventAdapter(block_event)
    dispatcher.dispatch(event)
    mock_handle.assert_called_once_with(event, agent)

def test_chat_event_handling(mocker,  mock_minecraft_service, configure_dependencies):
    dispatcher = EventDispatcher()

    handler = CustomEventHandler()
    agent = Agent("Test", PlaceBlockAction(), handler)
    dispatcher.register(handler,  agent)

    mock_handle = mocker.patch.object(handler, 'handle_chat_event')

    chat_event = ChatEvent.Post(2, "Hello World")
    event = ChatEventAdapter(chat_event)
    dispatcher.dispatch(event)
    mock_handle.assert_called_once_with(event, agent)