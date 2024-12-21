import pytest
from core.mcpi import minecraft
from unittest.mock import patch, MagicMock
from core.services.minecraft_service import MinecraftService

mm = MagicMock()

@pytest.fixture
def mock_minecraft_create():
    """Fixture para mockear minecraft.Minecraft.create"""
    with patch.object(minecraft.Minecraft, 'create', return_value=mm) as mock_create:
        yield mock_create

def test_singleton_instance(mock_minecraft_create):
    # Crear una instancia del servicio
    service1 = MinecraftService()
    service2 = MinecraftService()

    # Verificamos que ambas instancias sean la misma
    assert service1 is service2, "MinecraftService should be a singleton"

    # Verificamos que la conexión a Minecraft se haya creado solo una vez
    mock_minecraft_create.assert_called_once()

def test_minecraft_connection(mock_minecraft_create):
    # Crear la instancia del servicio
    service = MinecraftService()

    # Obtener la instancia mockeada de Minecraft
    mock_mc_instance = mock_minecraft_create.return_value

    # Verificamos que la instancia de Minecraft devuelta es la correcta
    mc_instance = service.get_instance()
    assert mc_instance is mock_mc_instance

    mc_instance.postToChat("Message from Minecraft")
    mock_mc_instance.postToChat.assert_called_once()