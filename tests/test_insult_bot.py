import pytest
from unittest.mock import MagicMock, patch

from agents.insult_bot import InsultAction, create_agent, CustomEventHandler
from core.agent import Agent
from core.di.container import DependencyContainer
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


insults = ["Insult 1", "Insult 2", "Insult 3"]

def test_insult_action(configure_dependencies):
    mock_agent = MagicMock(spec=Agent)
    mock_agent.minecraft = MagicMock()

    with patch('agents.insult_bot.insults', insults):
        action = InsultAction()
        action.execute(mock_agent)

        mock_agent.minecraft.send_message.assert_called_once()
        sent_message = mock_agent.minecraft.send_message.call_args[0][0]
        assert sent_message in insults


def test_custom_event_handler(configure_dependencies):
    mock_agent = MagicMock(spec=Agent)
    mock_event = MagicMock()

    handler = CustomEventHandler()
    handler.handle_chat_event(mock_event, mock_agent)

    mock_agent.run.assert_called_once()


def test_create_agent(configure_dependencies):
    with patch('agents.insult_bot.Agent') as MockAgent, \
            patch('agents.insult_bot.InsultAction') as MockInsultAction, \
            patch('agents.insult_bot.CustomEventHandler') as MockCustomEventHandler:
        mock_agent_instance = MockAgent.return_value
        agent = create_agent()

        MockAgent.assert_called_once_with("InsultBot", MockInsultAction.return_value,
                                          MockCustomEventHandler.return_value)
        mock_agent_instance.register_command.assert_not_called()

