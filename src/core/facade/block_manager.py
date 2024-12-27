from argparse import ArgumentError

from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.mcpi import block
from core.services.minecraft_service import MinecraftService


class BlockManager(Injectable):
    """
    Manages the methods associated with blocks within the world of Minecraft.
    """
    _ms: MinecraftService = inject(MinecraftService)

    def __init__(self):
        super().__init__()
        self.mc = self._ms.get_instance()

    def place_block(self, block_type : str, x : int, y : int, z : int):
        """
        Puts a block in a place, if block_type not exists, raise ArgumentError.

        Parameters
        ----------
        block_type : string
        x : int
        y : int
        z : int
        """
        if block_type in blocks:
            self.mc.setBlock(x, y, z, blocks[block_type])
        else:
            raise ArgumentError(None, message="Unknown block type")

    def destroy_block(self, x : int, y : int, z : int):
        """
        Place an air block in a specific position.

        Parameters
        ----------
        x : int
        y : int
        z : int
        """
        self.mc.setBlock(x, y, z, blocks["air"])

    def get_block(self, x : int, y : int, z : int):
        """
        Get block (x,y,z)

        Parameters
        ----------
        x : int
        y : int
        z : int

        Returns
        -------
        id : int
        """
        """"""
        return self.mc.getBlock(x, y, z)

    def get_block_data(self, x, y, z):
        """
        Get block data (x,y,z)

        Parameters
        ----------
        x : int
        y : int
        z : int

        Returns
        -------
        {id : int, data: int}
        """
        bl = self.mc.getBlockWithData(x, y, z)
        return {'id': bl.id, 'data': bl}


blocks = {
    "air": block.AIR,
    "stone": block.STONE,
    "grass": block.GRASS,
    "dirt": block.DIRT,
    "cobblestone": block.COBBLESTONE,
    "wood_planks": block.WOOD_PLANKS,
    "sapling": block.SAPLING,
    "bedrock": block.BEDROCK,
    "water_flowing": block.WATER_FLOWING,
    "water": block.WATER,
    "water_stationary": block.WATER_STATIONARY,
    "lava_flowing": block.LAVA_FLOWING,
    "lava": block.LAVA,
    "lava_stationary": block.LAVA_STATIONARY,
    "sand": block.SAND,
    "gravel": block.GRAVEL,
    "gold_ore": block.GOLD_ORE,
    "iron_ore": block.IRON_ORE,
    "coal_ore": block.COAL_ORE,
    "wood": block.WOOD,
    "leaves": block.LEAVES,
    "glass": block.GLASS,
    "lapis_lazuli_ore": block.LAPIS_LAZULI_ORE,
    "lapis_lazuli_block": block.LAPIS_LAZULI_BLOCK,
    "sandstone": block.SANDSTONE,
    "bed": block.BED,
    "cobweb": block.COBWEB,
    "grass_tall": block.GRASS_TALL,
    "wool": block.WOOL,
    "flower_yellow": block.FLOWER_YELLOW,
    "flower_cyan": block.FLOWER_CYAN,
    "mushroom_brown": block.MUSHROOM_BROWN,
    "mushroom_red": block.MUSHROOM_RED,
    "gold_block": block.GOLD_BLOCK,
    "iron_block": block.IRON_BLOCK,
    "stone_slab_double": block.STONE_SLAB_DOUBLE,
    "stone_slab": block.STONE_SLAB,
    "brick_block": block.BRICK_BLOCK,
    "tnt": block.TNT,
    "bookshelf": block.BOOKSHELF,
    "moss_stone": block.MOSS_STONE,
    "obsidian": block.OBSIDIAN,
    "torch": block.TORCH,
    "fire": block.FIRE,
    "stairs_wood": block.STAIRS_WOOD,
    "chest": block.CHEST,
    "diamond_ore": block.DIAMOND_ORE,
    "diamond_block": block.DIAMOND_BLOCK,
    "crafting_table": block.CRAFTING_TABLE,
    "farmland": block.FARMLAND,
    "furnace_inactive": block.FURNACE_INACTIVE,
    "furnace_active": block.FURNACE_ACTIVE,
    "door_wood": block.DOOR_WOOD,
    "ladder": block.LADDER,
    "stairs_cobblestone": block.STAIRS_COBBLESTONE,
    "door_iron": block.DOOR_IRON,
    "redstone_ore": block.REDSTONE_ORE,
    "snow": block.SNOW,
    "ice": block.ICE,
    "snow_block": block.SNOW_BLOCK,
    "cactus": block.CACTUS,
    "clay": block.CLAY,
    "sugar_cane": block.SUGAR_CANE,
    "fence": block.FENCE,
    "glowstone_block": block.GLOWSTONE_BLOCK,
    "bedrock_invisible": block.BEDROCK_INVISIBLE,
    "stone_brick": block.STONE_BRICK,
    "glass_pane": block.GLASS_PANE,
    "melon": block.MELON,
    "fence_gate": block.FENCE_GATE,
    "glowing_obsidian": block.GLOWING_OBSIDIAN,
    "nether_reactor_core": block.NETHER_REACTOR_CORE,
}
