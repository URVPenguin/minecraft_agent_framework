import pytest
from unittest.mock import MagicMock, patch

from core.action import Action
from core.agent import Agent
from core.di.container import DependencyContainer
from core.events.interfaces.event_handler import EventHandler
from core.services.command.interfaces.command import Command
from core.services.minecraft_service import MinecraftService


@pytest.fixture
def mock_action():
    return MagicMock(Action)


@pytest.fixture
def mock_event_handler():
    return MagicMock(EventHandler)


@pytest.fixture
def mock_command_handler():
    with patch('core.services.command.command_handler.CommandHandler') as MockCommandHandler:
        yield MockCommandHandler()


@pytest.fixture
def mock_minecraft_manager():
    with patch('core.facade.minecraft_manager.MinecraftManager') as MockMinecraftManager:
        yield MockMinecraftManager()

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


def test_register_command(mock_command_handler, configure_dependencies):
    agent = Agent("TestAgent")
    agent.command_handler = mock_command_handler

    mock_command = MagicMock(Command)
    agent.register_command("test_command", mock_command)

    mock_command_handler.register.assert_called_once_with("test_command", mock_command)


def test_handle_command(mock_command_handler, configure_dependencies):
    agent = Agent("TestAgent")
    agent.command_handler = mock_command_handler

    mock_command_name = "test_command"
    mock_args = (1, 2)
    mock_kwargs = {"key": "value"}

    agent.handle_command(mock_command_name, *mock_args, **mock_kwargs)

    mock_command_handler.execute.assert_called_once_with(mock_command_name, agent, *mock_args, **mock_kwargs)


def test_agent_run_with_action(mock_action, configure_dependencies):
    agent = Agent("TestAgent", action=mock_action)
    agent.run()

    mock_action.execute.assert_called_once_with(agent)


def test_agent_run_without_action(configure_dependencies):
    agent = Agent("TestAgent")
    agent.run()

    assert not agent.action
