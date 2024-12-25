from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.events.block_event_adapter import BlockEventAdapter
from core.events.chat_event_adapter import ChatEventAdapter
from core.events.event_dispatcher import EventDispatcher
from core.services.agent_loader_service import AgentLoaderService
from core.services.command.command_service import CommandService
from core.services.minecraft_service import MinecraftService

class CoreManager(Injectable):
    _ms: MinecraftService = inject(MinecraftService)
    _dispatcher: EventDispatcher = inject(EventDispatcher)
    _command_service: CommandService = inject(CommandService)
    _agent_loader_service: AgentLoaderService = inject(AgentLoaderService)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.agents = self._agent_loader_service.load_agents()
        self.mc = self._ms.get_instance()

    def listen(self):
        while True:
            block_hits = self.mc.events.pollBlockHits()
            for hit in block_hits:
                self._dispatcher.dispatch(BlockEventAdapter(hit))

            chat_posts = self.mc.events.pollChatPosts()
            for post in chat_posts:
                event = ChatEventAdapter(post)
                if not self._command_service.process_command(event):
                    self._dispatcher.dispatch(event)
