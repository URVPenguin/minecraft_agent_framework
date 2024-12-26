from time import sleep
from core.action import Action
from core.agent import Agent
from core.services.command.interfaces.command import Command

class DetonateAction(Action):
    def execute(self, agent: Agent):
        agent.place_block("tnt", 1, 0, 0)
        agent.place_block("fire", 1, 1, 0)

class TNTCommand(Command):
    def execute(self, agent, args, kwargs):
        if len(args) > 0 and args[0].isdigit():
            for i in range(int(args[0])):
                agent.run()
                sleep(1.5 if kwargs.get("time") is None else float(kwargs.get("time")))
        else:
            agent.run()

def create_agent():
    agent = Agent("TNTBot", DetonateAction())
    agent.register_command("@tnt", TNTCommand())
    return agent