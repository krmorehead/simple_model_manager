import pytest
from flask import Flask
from app import create_app
from typing import Generator
from flask.testing import FlaskClient
import io

@pytest.fixture
def client():
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

def test_list_languages(client) -> None:
    response = client.get('/languages')
    assert response.status_code == 200
    data = response.get_json()
    assert 'languages' in data
    assert isinstance(data['languages'], list)
    assert any(lang['code'] == 'en' and lang['name'] == 'English' for lang in data['languages'])

def test_translate_file_missing_fields(client) -> None:
    response = client.post('/translate', data={}, content_type='multipart/form-data')
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_translate_file_invalid_language_code(client) -> None:
    data = {
        'translate_from': 'xx',
        'translate_to': 'en',
        'export_format': 'json'
    }
    response = client.post('/translate', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_translate_file_invalid_export_format(client) -> None:
    data = {
        'translate_from': 'en',
        'translate_to': 'fr',
        'export_format': 'txt'
    }
    response = client.post('/translate', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_translate_file_invalid_file_format(monkeypatch, client) -> None:
    data = {
        'file': (io.BytesIO(b'not a valid file'), 'test.json'),
        'translate_from': 'en',
        'translate_to': 'fr',
        'export_format': 'json'
    }
    from app.services import file_parser
    monkeypatch.setattr(file_parser.FileParser, 'is_valid_format', lambda self, content: False)
    response = client.post('/translate', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_translate_file_success(monkeypatch, client) -> None:
    data = {
        'file': (io.BytesIO(b'{"a": 1}'), 'test.json'),
        'translate_from': 'en',
        'translate_to': 'fr',
        'export_format': 'json'
    }
    from app.services import file_parser
    monkeypatch.setattr(file_parser.FileParser, 'is_valid_format', lambda self, content: True)
    response = client.post('/translate', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert 'result' in response.get_json() 