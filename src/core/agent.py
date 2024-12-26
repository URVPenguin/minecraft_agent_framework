from core.action import Action
from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.events.default_event_handler import DefaultEventHandler
from core.events.interfaces.event_handler import EventHandler
from core.mcpi import block
from core.services.command.interfaces.command import Command
from core.services.minecraft_service import MinecraftService

class Agent(Injectable):
    _ms: MinecraftService = inject(MinecraftService)

    def __init__(self, name, action: Action = None, event_handler: EventHandler = None):
        super().__init__()
        self.name = name
        self.action = action
        self.event_handler = event_handler if event_handler is not None else DefaultEventHandler()
        self.commands = {}
        self.mc = self._ms.get_instance()
        self.mc.postToChat(f"Bot {name} created")

        self.blocks = {
            "air": block.AIR,
            "stone": block.STONE,
            "cobblestone": block.COBBLESTONE,
            "dirt": block.DIRT,
            "wood": block.WOOD,
            "sand": block.SAND,
            "diamond": block.DIAMOND_BLOCK,
            "glass": block.GLASS,
            "lava": block.LAVA,
            "water": block.WATER,
            "grass": block.GRASS,
            "tnt": block.TNT,
            "fire": block.FIRE
        }

    def register_command(self, command_name: str, command : Command):
        self.commands[command_name] = command

    def handle_command(self, command, *args, **kwargs):
        command = self.commands.get(command)
        if command:
            command.execute(self, *args, **kwargs)

    def run(self):
        if self.action:
            self.action.execute(self)

    def move(self, x, y, z):
        """
        Moves the agent to the given position
        """
        self.mc.player.setTilePos(x, y, z)

    def place_block(self, block_type, x_offset=0, y_offset=0, z_offset=0):
        """
        Place a block in the relative bot position
        """
        if block_type not in self.blocks:
            return

        pos = self.get_pos()
        x, y, z = pos.x + x_offset, pos.y + y_offset, pos.z + z_offset
        self.mc.setBlock(x, y, z, self.blocks[block_type])

    def place_block_in(self, block_type, x, y, z):
        """
        Place a block in any position
        """
        if block_type not in self.blocks:
            return

        self.mc.setBlock(x, y, z, self.blocks[block_type])

    def get_pos(self):
        return self.mc.player.getTilePos()

    def destroy_block(self, x_offset=0, y_offset=0, z_offset=0):
        """
        Destroys a block in the relative bot position
        """
        pos = self.get_pos()
        x, y, z = pos.x + x_offset, pos.y + y_offset, pos.z + z_offset
        self.mc.setBlock(x, y, z, self.blocks["air"])

    def message(self, message):
        """
        The bot sends message to the chat
        """
        self.mc.postToChat(message)