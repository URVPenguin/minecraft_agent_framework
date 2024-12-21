from core.di.decorators.dependency import dependency
from core.mcpi import minecraft

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
        if not hasattr(self, 'mc'):
            self.host = host
            self.port = port
            try:
                self.mc = minecraft.Minecraft.create()
            except ConnectionError as ce:
                exit("Could not connect to Minecraft. Error: " + ce.strerror)

    def get_instance(self):
        """
        Get Minecraft instance.

        Returns
        -------
        mc: Minecraft
            :class:`Minecraft` instance.
        """
        return self.mc