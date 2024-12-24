from agents.custom_bot import create_agent
from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.events.block_event_adapter import BlockEventAdapter
from core.events.chat_event_adapter import ChatEventAdapter
from core.events.event_dispatcher import EventDispatcher
from core.services.minecraft_service import MinecraftService

class CoreManager(Injectable):
    _ms: MinecraftService = inject(MinecraftService)
    _dispatcher: EventDispatcher = inject(EventDispatcher)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.agent = create_agent()
        self._dispatcher.register(self.agent.event_handler, self.agent)
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
        self.agent.run()
        while True:
            block_hits = mc.events.pollBlockHits()
            for hit in block_hits:
                self._dispatcher.dispatch(BlockEventAdapter(hit))

            chat_posts = mc.events.pollChatPosts()
            for post in chat_posts:
                self._dispatcher.dispatch(ChatEventAdapter(post))
