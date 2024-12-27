from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.services.minecraft_service import MinecraftService

class PlayerManager(Injectable):
    """
    Manages the methods associated with player within the world of Minecraft.
    """
    _ms: MinecraftService = inject(MinecraftService)

    def __init__(self):
        super().__init__()
        self.mc = self._ms.get_instance()

    def get_position(self):
        """
        Returns the current position of the player.

        Returns
        -------
        Vec3
        """
        return self.mc.player.getTilePos()

    def set_position(self, x : int, y : int, z : int):
        """
        Sets a new player position.

        Parameters
        ----------
        x : int
        y : int
        z : int
        """
        self.mc.player.setTilePos(x, y, z)

    def get_direction(self):
        """
        Returns the current direction of the player.

        Returns
        -------
        Vec3
        """
        return self.mc.player.getDirection()

    def get_rotation(self):
        """
        Returns the current rotation of the player.

        Returns
        -------
        float
        """
        return self.mc.player.getRotation()

    def get_pitch(self):
        """
        Returns the current pitch of the player.

        Returns
        -------
        float
        """
        return self.mc.player.getPitch()