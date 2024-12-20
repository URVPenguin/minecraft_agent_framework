from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.services.minecraft_service import MinecraftService


class CoreManager(Injectable):
    _ms: MinecraftService = inject(MinecraftService)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    #     self.agents = []
    #     self.messages = []
    #
    #     self.agent_loader = AgentLoader()
    #     self.agent_loader.load_agents()
    #     self.command_processor = CommandProcessor(self, self.agent_loader)
    #
    #
    #
    # def add_agent(self, agent):
    #     self.agents.append(agent)
    #
    # def send_message(self, message: str):
    #     print(f"Mensaje recibido en el chat: {message}")
    #     self.messages.append(message)
    #     self.notify_agents(message)
    #
    # def notify_agents(self, message: str):
    #     for agent in self.agents:
    #         agent.run(message)

    def listen(self):
        mc = self._ms.get_instance()
        while True:
            chats = mc.events.pollChatPosts()
            for chat in chats:
                mc.postToChat(f"Missatge: {chat.message} rebut!!")
