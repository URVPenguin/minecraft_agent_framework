from core.action import Action
from core.events.default_event_handler import DefaultEventHandler
from core.events.interfaces.event_handler import EventHandler
from core.facade.minecraft_manager import MinecraftManager
from core.services.command.command_handler import CommandHandler
from core.services.command.interfaces.command import Command


class Agent:
    def __init__(self, name, action: Action = None, event_handler: EventHandler = None):
        super().__init__()
        self.name = name
        self.action = action
        self.event_handler = event_handler if event_handler is not None else DefaultEventHandler()
        self.command_handler = CommandHandler()
        self.minecraft = MinecraftManager()
        self.minecraft.send_message(f"Bot {name} created")

    def register_command(self, command_name: str, command: Command):
        self.command_handler.register(command_name, command)

    def handle_command(self, command_name, *args, **kwargs):
        self.command_handler.execute(command_name, self, *args, **kwargs)

    def run(self):
        if self.action:
            self.action.execute(self)