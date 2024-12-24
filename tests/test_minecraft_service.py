import pytest
from core.mcpi import minecraft
from unittest.mock import patch, MagicMock
from core.services.minecraft_service import MinecraftService

mm = MagicMock()

@pytest.fixture
def mock_minecraft_create():
    with patch.object(minecraft.Minecraft, 'create', return_value=mm) as mock_create:
        yield mock_create

def test_singleton_instance(mock_minecraft_create):
    service1 = MinecraftService()
    service2 = MinecraftService()
    assert service1 is service2, "MinecraftService should be a singleton"
    mock_minecraft_create.assert_called_once()

def test_minecraft_connection(mock_minecraft_create):
    service = MinecraftService()
    mock_mc_instance = mock_minecraft_create.return_value
    mc_instance = service.get_instance()
    assert mc_instance is mock_mc_instance
    mc_instance.postToChat("Message from Minecraft")
    mock_mc_instance.postToChat.assert_called_once()