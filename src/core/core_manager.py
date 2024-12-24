from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.events.block_event_adapter import BlockEventAdapter
from core.events.chat_event_adapter import ChatEventAdapter
from core.events.event_dispatcher import EventDispatcher
from core.events.interfaces.event_handler import EventHandler
from core.services.minecraft_service import MinecraftService

class BlockEventHandler(EventHandler):
    def handle_block_event(self, event):
        print(f"BlockEventHandler: Bloque golpeado en posición {event.pos}, por entidad {event.entityId}")

    def handle_chat_event(self, event):
        # No hace nada con eventos de chat
        pass

class ChatEventHandler(EventHandler):
    def handle_block_event(self, event):
        # No hace nada con eventos de bloques
        pass

    def handle_chat_event(self, event):
        print(f"ChatEventHandler: Entidad {event.entityId} dijo '{event.message}'")


class CoreManager(Injectable):
    _ms: MinecraftService = inject(MinecraftService)
    _dispatcher: EventDispatcher = inject(EventDispatcher)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._dispatcher.register(BlockEventHandler())
        self._dispatcher.register(ChatEventHandler())
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
            block_hits = mc.events.pollBlockHits()
            for hit in block_hits:
                self._dispatcher.dispatch(BlockEventAdapter(hit))

            chat_posts = mc.events.pollChatPosts()
            for post in chat_posts:
                self._dispatcher.dispatch(ChatEventAdapter(post))
