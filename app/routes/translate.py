from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, fields
from app.services.model_service import ModelService
from config.settings import Config
from app.utils.language_codes import get_supported_languages, get_language_name, is_valid_language_code
from app.services.file_parser import FileParser
import os
import tempfile
import yaml

translate_bp = Blueprint('translate', __name__)
api = Api(translate_bp, doc='/docs', title='Simple Model Manager API', description='Translation and language model management API')
ns = api.namespace('translate', description='Translation operations')

model_service = ModelService(Config())

translate_request = api.model('TranslateRequest', {
    'text': fields.String(required=True),
    'source_lang': fields.String(required=True),
    'target_lang': fields.String(required=True)
})

translate_response = api.model('TranslateResponse', {
    'translation': fields.String
})

languages_response = api.model('LanguagesResponse', {
    'languages': fields.List(fields.Nested(api.model('Language', {
        'code': fields.String,
        'name': fields.String
    })))
})

@ns.route('/')
class TranslateResource(Resource):
    @api.expect(translate_request, validate=True)
    @api.marshal_with(translate_response, code=200)
    def post(self):
        """Translate text from source_lang to target_lang"""
        try:
            data = request.get_json()
            text = data.get('text')
            source_lang = data.get('source_lang')
            target_lang = data.get('target_lang')
            if not text or not source_lang or not target_lang:
                api.abort(400, 'Missing required fields')
            if not is_valid_language_code(source_lang) or not is_valid_language_code(target_lang):
                api.abort(400, 'Invalid language code')
            result = model_service.translate(text, source_lang, target_lang)
            return {'translation': result}, 200
        except Exception:
            api.abort(500, 'Internal server error')

@ns.route('/languages')
class LanguagesResource(Resource):
    @api.marshal_with(languages_response, code=200)
    def get(self):
        """List supported languages"""
        try:
            codes = get_supported_languages()
            languages = [{"code": code, "name": get_language_name(code)} for code in codes]
            return {"languages": languages}, 200
        except Exception:
            api.abort(500, 'Internal server error') 