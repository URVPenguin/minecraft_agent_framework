import pytest
from unittest.mock import MagicMock, patch

from core.core_manager import CoreManager
from core.di.container import DependencyContainer
from core.events.event_dispatcher import EventDispatcher
from core.services.agent_loader_service import AgentLoaderService
from core.services.command.command_service import CommandService
from core.services.minecraft_service import MinecraftService


@pytest.fixture
def mock_minecraft_service():
    mock_service = MagicMock(MinecraftService)
    mock_instance = MagicMock()
    mock_service.get_instance.return_value = mock_instance
    return mock_service, mock_instance


@pytest.fixture
def mock_event_dispatcher():
    mock = MagicMock(EventDispatcher)
    mock.dispatch = MagicMock()
    return mock


@pytest.fixture
def mock_command_service():
    return MagicMock(CommandService)


@pytest.fixture
def mock_agent_loader():
    mock_loader = MagicMock(spec=AgentLoaderService)
    mock_loader.load_agents.return_value = ["agent1", "agent2"]
    return mock_loader


@pytest.fixture
def configure_dependencies(mock_minecraft_service, mock_event_dispatcher, mock_command_service, mock_agent_loader):
    mock_service, mock_instance = mock_minecraft_service

    # Reset the DependencyContainer to ensure no residual state from other tests
    container = DependencyContainer()
    container._registrations = {}
    container.register(MinecraftService, lambda: mock_service)
    container.register(EventDispatcher, lambda: mock_event_dispatcher)
    container.register(CommandService, lambda: mock_command_service)
    container.register(AgentLoaderService, lambda: mock_agent_loader)
    return mock_service, mock_instance


def test_core_manager_init(configure_dependencies, mock_minecraft_service, mock_event_dispatcher, mock_command_service, mock_agent_loader):
    mock_service, mock_instance = configure_dependencies
    manager = CoreManager()
    assert manager.agents.__eq__(["agent1", "agent2"])
    assert manager.mc == mock_instance


