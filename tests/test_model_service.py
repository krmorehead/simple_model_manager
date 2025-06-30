import pytest
from app.services.model_service import ModelService
from config.settings import Config

@pytest.fixture
def model_service() -> ModelService:
    return ModelService(Config())

def test_model_service_init(model_service: ModelService) -> None:
    assert model_service.model is None

def test_translate_stub(model_service: ModelService) -> None:
    result = model_service.translate("hello", "en", "fr")
    assert result == "" 