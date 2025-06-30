import pytest
from flask import Flask
from app import create_app

@pytest.fixture
def client() -> Flask:
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_translate_valid(client) -> None:
    response = client.post('/translate', json={
        'text': 'hello',
        'source_lang': 'en',
        'target_lang': 'fr'
    })
    assert response.status_code == 200
    assert 'translation' in response.get_json()

def test_translate_missing_field(client) -> None:
    response = client.post('/translate', json={
        'text': 'hello',
        'source_lang': 'en'
    })
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_translate_internal_error(monkeypatch, client) -> None:
    def raise_exception(*args, **kwargs):
        raise Exception('fail')
    from app.routes import translate
    monkeypatch.setattr(translate.model_service, 'translate', raise_exception)
    response = client.post('/translate', json={
        'text': 'hello',
        'source_lang': 'en',
        'target_lang': 'fr'
    })
    assert response.status_code == 500
    assert 'error' in response.get_json() 