from unittest.mock import MagicMock, patch
from core.services.command.command_handler import CommandHandler
from core.services.command.interfaces.command import Command


class TestCommand(Command):
    def execute(self, agent, args, kwargs):
        pass

def test_command_handler_register_and_execute():
    handler = CommandHandler()

    mock_command = MagicMock(spec=TestCommand)

    mock_agent = MagicMock()
    mock_args = (1, 2)
    mock_kwargs = {'key': 'value'}

    handler.register("test_command", mock_command)

    assert "test_command" in handler.commands
    assert handler.commands["test_command"] == mock_command

    handler.execute("test_command", mock_agent, *mock_args, **mock_kwargs)

    mock_command.execute.assert_called_once_with(mock_agent, *mock_args, **mock_kwargs)




