import pytest
from unittest.mock import MagicMock, patch

from agents.tnt_bot import DetonateAction, TNTCommand, create_agent
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


def test_detonate_action():
    mock_agent = MagicMock(spec=Agent)
    mock_agent.minecraft = MagicMock()
    mock_agent.minecraft.player.get_position.return_value = (10, 64, 10)

    action = DetonateAction()
    action.execute(mock_agent)

    mock_agent.minecraft.blocks.place_block.assert_any_call("tnt", 11, 64, 10)
    mock_agent.minecraft.blocks.place_block.assert_any_call("fire", 11, 65, 10)


def test_tnt_command():
    mock_agent = MagicMock(spec=Agent)
    mock_agent.run = MagicMock()

    command = TNTCommand()

    with patch('agents.tnt_bot.TNTCommand', return_value=None):
        command.execute(mock_agent, ['3'], {'time': '0'})
        assert mock_agent.run.call_count == 3

    command.execute(mock_agent, [], {})
    mock_agent.run.assert_called()


def test_create_agent(configure_dependencies):
    with patch('agents.tnt_bot.Agent') as MockAgent, \
            patch('agents.tnt_bot.DetonateAction') as MockDetonateAction, \
            patch('agents.tnt_bot.TNTCommand') as MockTNTCommand:
        mock_agent_instance = MockAgent.return_value
        agent = create_agent()

        MockAgent.assert_called_once_with("TNTBot", MockDetonateAction.return_value)
        mock_agent_instance.register_command.assert_called_once_with("@tnt", MockTNTCommand.return_value)
