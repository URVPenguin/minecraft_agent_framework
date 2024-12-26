from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.services.minecraft_service import MinecraftService

class CameraManager(Injectable):
    _ms: MinecraftService = inject(MinecraftService)

    def __init__(self):
        super().__init__()
        self.mc = self._ms.get_instance()

    def normal_mode(self, *args):
        """Set camera mode to normal Minecraft view ([entityId])"""
        self.mc.camera.setNormal(args)

    def fixed_mode(self):
        """Set camera mode to fixed view"""
        self.mc.camera.setFixed()

    def follow_mode(self, *args):
        """Set camera mode to follow an entity ([entityId])"""
        self.mc.camera.setFollow(args)

    def custom_pos(self, *args):
        """Set camera entity position (x,y,z)"""
        self.mc.camera.setPos(args)
