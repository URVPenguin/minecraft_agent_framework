from argparse import ArgumentError
from unittest.mock import MagicMock, patch

import pytest

from core.di.container import DependencyContainer
from core.facade.block_manager import BlockManager
from core.facade.camera_manager import CameraManager
from core.facade.minecraft_manager import MinecraftManager
from core.facade.player_manager import PlayerManager
from core.services.minecraft_service import MinecraftService


@pytest.fixture
def mock_minecraft_service():
    mock_service = MagicMock(MinecraftService)
    mock_instance = MagicMock()

    mock_service.get_instance.return_value = mock_instance

    return mock_service, mock_instance

@pytest.fixture
def configure_dependencies(mock_minecraft_service):
    mock_service, mock_instance = mock_minecraft_service
    DependencyContainer()._registrations = {}
    DependencyContainer().register(MinecraftService, mock_service)

    return mock_service, mock_instance


@pytest.fixture
def minecraft_manager(mock_minecraft_service):
    with patch('core.facade.minecraft_manager.PlayerManager', new=MagicMock()), \
         patch('core.facade.minecraft_manager.BlockManager', new=MagicMock()), \
         patch('core.facade.minecraft_manager.CameraManager', new=MagicMock()):
        return MinecraftManager()

@pytest.fixture
def player_manager(configure_dependencies):
    return PlayerManager()

@pytest.fixture
def camera_manager(configure_dependencies):
    return CameraManager()

@pytest.fixture
def block_manager(configure_dependencies):
    return BlockManager()

def test_send_message(minecraft_manager, configure_dependencies):
    minecraft_manager.send_message("Hello, Minecraft!")
    minecraft_manager.mc.postToChat.assert_called_once_with("Hello, Minecraft!")

def test_world_settings(minecraft_manager):
    minecraft_manager.world_settings("world_immutable", True)
    minecraft_manager.mc.setting.assert_called_once_with("world_immutable", True)

def test_save_checkpoint(minecraft_manager):
    minecraft_manager.save_checkpoint()
    minecraft_manager.mc.saveCheckpoint.assert_called_once()

def test_restore_checkpoint(minecraft_manager):
    minecraft_manager.restore_checkpoint()
    minecraft_manager.mc.restoreCheckpoint.assert_called_once()

def test_word_height(minecraft_manager):
    minecraft_manager.word_height(10, 20)
    minecraft_manager.mc.getHeight.assert_called_once_with((10, 20))

def test_get_players_ids(minecraft_manager):
    minecraft_manager.get_players_ids()
    minecraft_manager.mc.getPlayerEntityIds.assert_called_once()

def test_get_player_id(minecraft_manager):
    minecraft_manager.get_player_id("player1")
    minecraft_manager.mc.getPlayerEntityId.assert_called_once_with("player1")

def test_get_position(player_manager):
    player_manager.get_position()
    player_manager.mc.player.getTilePos.assert_called_once()

def test_set_position(player_manager):
    player_manager.set_position(0,0,0)
    player_manager.mc.player.setTilePos.assert_called_once()

def test_get_direction(player_manager):
    player_manager.get_direction()
    player_manager.mc.player.getDirection.assert_called_once()

def test_get_rotation(player_manager):
    player_manager.get_rotation()
    player_manager.mc.player.getRotation.assert_called_once()

def test_get_pitch(player_manager):
    player_manager.get_pitch()
    player_manager.mc.player.getPitch.assert_called_once()

def test_normal_mode(camera_manager):
    camera_manager.normal_mode()
    camera_manager.mc.camera.setNormal.assert_called_once()

def test_fixed_mode(camera_manager):
    camera_manager.fixed_mode()
    camera_manager.mc.camera.setFixed.assert_called_once()

def test_follow_mode(camera_manager):
    camera_manager.follow_mode()
    camera_manager.mc.camera.setFollow.assert_called_once()

def test_custom_pos(camera_manager):
    camera_manager.custom_pos()
    camera_manager.mc.camera.setPos.assert_called_once()

def test_place_block(block_manager):
    block_manager.place_block("air", 0, 0, 0)
    block_manager.mc.setBlock.assert_called_once()

def test_place_block_argument_error(block_manager):
    with pytest.raises(ArgumentError, match="Unknown block type"):
        block_manager.place_block("unknown", 0, 0, 0)

def test_destroy_block(block_manager):
    block_manager.destroy_block( 0, 0, 0)
    block_manager.mc.setBlock.assert_called_once()

def test_get_block(block_manager):
    block_manager.get_block( 0, 0, 0)
    block_manager.mc.getBlock.assert_called_once()

def test_get_block_data(block_manager):
    block_manager.get_block_data( 0, 0, 0)
    block_manager.mc.getBlockWithData.assert_called_once()
