import pytest
from unittest.mock import MagicMock, patch

from agents.chat_bot import CustomEventHandler, create_agent
from core.agent import Agent
from core.di.container import DependencyContainer
from core.events.chat_event_adapter import ChatEventAdapter
from core.services.minecraft_service import MinecraftService


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

def test_custom_event_handler(configure_dependencies):
    mock_agent = MagicMock(spec=Agent)
    mock_event = MagicMock(spec=ChatEventAdapter)
    mock_agent.minecraft = MagicMock()
    mock_event.get_data.return_value = "Hello, world!"

    with patch('agents.chat_bot.ask', return_value="Mocked response"):
        handler = CustomEventHandler()
        handler.handle_chat_event(mock_event, mock_agent)

        mock_agent.minecraft.send_message.assert_called_once_with("Mocked response")


def test_create_agent(configure_dependencies):
    with patch('agents.chat_bot.Agent') as MockAgent, \
            patch('agents.chat_bot.CustomEventHandler') as MockCustomEventHandler:
        mock_agent_instance = MockAgent.return_value
        agent = create_agent()

        MockAgent.assert_called_once_with("ChatBot", None, MockCustomEventHandler.return_value)
        mock_agent_instance.register_command.assert_not_called()


