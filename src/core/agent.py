from core.action import Action
from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.events.interfaces.event_handler import EventHandler
from core.mcpi import block
from core.services.minecraft_service import MinecraftService

class Agent(Injectable):
    _ms: MinecraftService = inject(MinecraftService)

    def __init__(self, name, action: Action, event_handler: EventHandler):
        super().__init__()
        self.name = name
        self.action = action
        self.event_handler = event_handler
        self.mc = self._ms.get_instance()
        self.pos = self.mc.player.getTilePos()
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
        }

    def run(self):
        self.action.execute(self)

    def move(self, x, y, z):
        """
        Moves the agent to the given position
        """
        self.mc.player.setTilePos(x, y, z)
        self.pos = self.mc.player.getTilePos()

    def place_block(self, block_type, x_offset=0, y_offset=0, z_offset=0):
        """
        Place a block in the relative bot position
        """
        if block_type not in self.blocks:
            return

        x, y, z = self.pos.x + x_offset, self.pos.y + y_offset, self.pos.z + z_offset
        self.mc.setBlock(x, y, z, self.blocks[block_type])

    def place_block_in(self, block_type, x, y, z):
        """
        Place a block in any position
        """
        if block_type not in self.blocks:
            return

        self.mc.setBlock(x, y, z, self.blocks[block_type])

    def destroy_block(self, x_offset=0, y_offset=0, z_offset=0):
        """
        Destroys a block in the relative bot position
        """
        x, y, z = self.pos.x + x_offset, self.pos.y + y_offset, self.pos.z + z_offset
        self.mc.setBlock(x, y, z, self.blocks["air"])

    def message(self, message):
        """
        The bot sends message to the chat
        """
        self.mc.postToChat(message)