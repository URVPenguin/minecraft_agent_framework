from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.services.minecraft_service import MinecraftService

class PlayerManager(Injectable):
    _ms: MinecraftService = inject(MinecraftService)

    def __init__(self):
        super().__init__()
        self.mc = self._ms.get_instance()

    def get_position(self):
        return self.mc.player.getTilePos()

    def set_position(self, x, y, z):
        self.mc.player.setTilePos(x, y, z)

    def get_direction(self):
        return self.mc.player.getDirection()

    def get_rotation(self):
        return self.mc.player.getRotation()

    def get_pitch(self):
        return self.mc.player.getPitch()