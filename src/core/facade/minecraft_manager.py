from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.facade.block_manager import BlockManager
from core.facade.camera_manager import CameraManager
from core.facade.player_manager import PlayerManager
from core.services.minecraft_service import MinecraftService

class MinecraftManager(Injectable):
    _ms: MinecraftService = inject(MinecraftService)

    def __init__(self):
        super().__init__()
        self.mc = self._ms.get_instance()
        self.player = PlayerManager()
        self.blocks = BlockManager()
        self.camera = CameraManager()

    def send_message(self, message):
        """
        Sends message to minecraft server

        Parameters
        ----------
        message
        """
        self.mc.postToChat(message)

    def world_settings(self, setting, status):
        """Set a world setting (setting, status). keys: world_immutable, nametags_visible"""
        self.mc.setting(setting, status)

    def save_checkpoint(self):
        """Save a checkpoint that can be used for restoring the world"""
        self.mc.saveCheckpoint()

    def restore_checkpoint(self):
        """Restore the world state to the checkpoint"""
        self.mc.restoreCheckpoint()

    def word_height(self, *args):
        """Get the height of the world (x,z) => int"""
        return self.mc.getHeight(args)

    def get_players_ids(self):
        """Get the entity ids of the connected players => [id:int]"""
        return self.mc.getPlayerEntityIds()

    def get_player_id(self, name):
        """Get the entity id of the named player => [id:int]"""
        return self.mc.getPlayerEntityId(name)
