from time import sleep
from core.action import Action
from core.agent import Agent
from core.services.command.interfaces.command import Command

class DetonateAction(Action):
    def execute(self, agent: Agent):
        x,y,z = agent.minecraft.player.get_position()
        agent.minecraft.blocks.place_block("tnt", x+1, y, z)
        agent.minecraft.blocks.place_block("fire", x+1, y+1, z)

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