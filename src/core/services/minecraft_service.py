from core.di.decorators.dependency import dependency
from core.mcpi import minecraft
from core.mcpi.minecraft import Minecraft


@dependency
class MinecraftService:
    """
    Minecraft Service Singleton, that establish connection to Minecraft.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, host = "localhost", port = 4711):
        self.host = host
        self.port = port
        self.mc = minecraft.Minecraft.create()

    def get_instance(self) -> Minecraft:
        """
        Get Minecraft instance.

        Returns
        -------
        mc: Minecraft
            Minecraft instance.
        """
        return self.mc