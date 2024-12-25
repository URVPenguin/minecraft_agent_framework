import pytest
from core.action import Action
from core.agent import Agent
from core.di.container import DependencyContainer
from core.events.chat_event_adapter import ChatEventAdapter
from core.events.event_dispatcher import EventDispatcher
from core.events.interfaces.event_handler import EventHandler
from core.mcpi.event import ChatEvent
from core.services.command.command_service import CommandService
from unittest.mock import MagicMock, patch

from core.services.minecraft_service import MinecraftService

class CustomEventHandler(EventHandler):
    def handle_block_event(self, event, agent):
        print(f"BlockEventHandler: Block hit in {event.get_data()}, by entity: {event.get_entity_id()}")

    def handle_chat_event(self, event, agent):
        print(f"ChatEventHandler: Entity: {event.get_entity_id()} says '{event.get_data()}'")

    def handle_command_event(self, event, agent):
        print(f"ChatEventHandler: Entity: {event.get_entity_id()} says '{event.get_data()}'")

class PlaceBlockAction(Action):
    def execute(self, agent: Agent):
        print(f"{agent.name} action'")

chat_event_exit = ChatEvent.Post(1, "@exit")
chat_event_unk = ChatEvent.Post(1, "unknown")
adap_exit = ChatEventAdapter(chat_event_exit)
adap_unk = ChatEventAdapter(chat_event_unk)

@pytest.fixture
def mock_minecraft_service():
    mock_service = MagicMock(MinecraftService)
    mock_instance = MagicMock()

    mock_service.get_instance.return_value = mock_instance
    mock_service.close = MagicMock()
    mock_instance.player.getTilePos.return_value = MagicMock(x=0, y=0, z=0)
    mock_instance.setBlock = MagicMock()
    mock_instance.postToChat = MagicMock()

    return mock_service, mock_instance

@pytest.fixture
def configure_dependencies(mock_minecraft_service, mocker):
    mock_service, _ = mock_minecraft_service
    DependencyContainer()._registrations = {}
    DependencyContainer().register(MinecraftService, mock_service)
    DependencyContainer().register(EventDispatcher, EventDispatcher())
    handler = CustomEventHandler()
    agent = Agent("Test", PlaceBlockAction(), handler)
    EventDispatcher().handlers = {}
    EventDispatcher().register(handler, agent)
    mock_handle = mocker.patch.object(handler, 'handle_command_event')
    return mock_handle, mock_service


@pytest.fixture
def command_service(configure_dependencies):
    command_service = CommandService()
    return command_service

def test_process_exit(command_service):
    with patch('sys.exit') as mock_exit:
        result = command_service.process_command(adap_exit)
        mock_exit.assert_called_once()

    assert result is True

def test_process_unknown(command_service):
    result = command_service.process_command(adap_unk)
    assert result is False