import pytest
from app.services.translation_service import TranslationService

@pytest.fixture
def service() -> TranslationService:
    return TranslationService()

def test_build_prompt_stub(service: TranslationService) -> None:
    assert service.build_prompt('text', 'English', 'French') == ''

def test_batch_translate_stub(service: TranslationService) -> None:
    items = [{"text": "hello", "source_language": "English", "target_language": "French"}]
    assert service.batch_translate(items) == []

def test_handle_error_stub(service: TranslationService) -> None:
    assert service.handle_error(Exception('fail')) == 'Translation error'

def test_cache_result_and_get_cached_result_stub(service: TranslationService) -> None:
    service.cache_result('key', 'result')
    assert service.get_cached_result('key') == '' 