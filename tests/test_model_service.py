import pytest
from app.services.model_service import ModelService
from config.settings import Config
from app.utils import language_codes

@pytest.fixture
def model_service() -> ModelService:
    return ModelService(Config())

def test_model_service_init(model_service: ModelService) -> None:
    assert model_service.model is None

def test_translate_stub(model_service: ModelService) -> None:
    result = model_service.translate("hello", "en", "fr")
    assert result == ""

def test_is_valid_language_code() -> None:
    assert language_codes.is_valid_language_code('en') is True
    assert language_codes.is_valid_language_code('xx') is False

def test_get_supported_languages() -> None:
    codes = language_codes.get_supported_languages()
    assert isinstance(codes, list)
    assert 'en' in codes

def test_get_language_name() -> None:
    assert language_codes.get_language_name('en') == 'English'
    assert language_codes.get_language_name('xx') == '' 