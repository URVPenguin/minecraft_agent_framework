from core.action import Action
from core.agent import Agent
from core.events.block_event_adapter import BlockEventAdapter
from core.events.chat_event_adapter import ChatEventAdapter
from core.events.comand_event import CommandEvent
from core.events.interfaces.event_handler import EventHandler
from core.services.command.interfaces.command import Command


class PlaceBlockAction(Action):
    def execute(self, agent: Agent):
        agent.place_block("stone", 1, 1, 0)
        agent.message(f"Bloc placed by {agent.name}")

class CustomEventHandler(EventHandler):
    def handle_block_event(self, event: BlockEventAdapter, agent: Agent):
        pos = event.get_data()
        agent.place_block_in("stone", pos.x, pos.y, pos.z)

    def handle_chat_event(self, event: ChatEventAdapter, agent: Agent):
        agent.message(f"Missatge rebut {event.get_data()}")

    def handle_command_event(self, event: CommandEvent, agent):
        command, args, kwargs = event.get_data().values()
        agent.handle_command(command, args, kwargs)

class HelloCommand(Command):
    def execute(self, agent, *args, **kwargs):
        agent.message("Hello Command !!!!!")

def create_agent():
    agent = Agent("CustomBot", PlaceBlockAction(), CustomEventHandler())
    agent.register_command("@hello", HelloCommand())
    return agent