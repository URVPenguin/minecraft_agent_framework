import pytest
from unittest.mock import MagicMock, patch, mock_open
from core.di.container import DependencyContainer
from core.events.event_dispatcher import EventDispatcher
from core.services.agent_loader_service import AgentLoaderService

@pytest.fixture
def mock_importlib():
    with patch("core.services.agent_loader_service.importlib") as mock_importlib:
        yield mock_importlib


@pytest.fixture
def mock_yaml():
    with patch("core.services.agent_loader_service.yaml.safe_load") as mock_yaml_load:
        yield mock_yaml_load


@pytest.fixture
def conf_dependencies():
    DependencyContainer()._registrations = {}
    DependencyContainer().register(EventDispatcher)

def test_load_agents(conf_dependencies, mock_importlib, mock_yaml):
    agent_loader = AgentLoaderService()
    # Mock YAML load
    mock_yaml.return_value = {"agents": {"test_agent": "test.module.path"}}

    # Mock importlib
    mock_module = MagicMock()
    mock_create_agent = MagicMock()
    mock_module.create_agent = mock_create_agent
    mock_importlib.import_module.return_value = mock_module

    # Mock open file
    m = mock_open(read_data="agents:\n  test_agent: 'test.module.path'")
    with patch("builtins.open", m):
        # Call the load_agents method
        agents = agent_loader.load_agents()

    # Assertions
    mock_importlib.import_module.assert_called_once_with("test.module.path")
    mock_create_agent.assert_called_once()
    assert len(agents) == 1
    assert agents[0] == mock_create_agent.return_value


def test_load_agents_exception(conf_dependencies, mock_importlib, mock_yaml):
    agent_loader = AgentLoaderService()
    # Mock YAML load
    mock_yaml.return_value = {"agents": {"test_agent": "test.module.path"}}

    # Mock importlib
    mock_module = MagicMock()
    mock_create_agent = MagicMock()
    mock_module.create_agent = mock_create_agent
    mock_importlib.import_module.return_value = mock_module

    # Mock open file
    m = mock_open(read_data="agents:\n  test_agent: 'test.module.path'")
    with patch("builtins.open", m):
        # Call the load_agents method
        agents = agent_loader.load_agents()

    # Assertions
    mock_importlib.import_module.assert_called_once_with("test.module.path")
    mock_create_agent.assert_called_once()
    assert len(agents) == 1
    assert agents[0] == mock_create_agent.return_value


def test_load_agents_module_not_found(conf_dependencies, mock_importlib, mock_yaml):
    # Mock YAML load
    mock_yaml.return_value = {"agents": {"test_agent": "non.existent.module"}}

    mock_importlib.import_module.side_effect = ModuleNotFoundError("Module not found")

    # Mock open file
    m = mock_open(read_data="agents:\n  test_agent: 'non.existent.module'")
    with patch("builtins.open", m):
        agents = AgentLoaderService().load_agents()

    # Assertions
    mock_importlib.import_module.assert_called_once_with("non.existent.module")
    assert len(agents) == 0

