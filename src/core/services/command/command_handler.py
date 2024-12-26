from core.services.command.interfaces.command import Command


class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute(self, command_name, agent, *args, **kwargs):
        command = self.commands.get(command_name)
        if command:
            command.execute(agent, *args, **kwargs)