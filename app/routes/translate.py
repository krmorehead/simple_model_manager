from flask import Blueprint, request, jsonify, current_app
from app.services.model_service import ModelService
from config.settings import Config
from app.utils.language_codes import get_supported_languages, get_language_name, is_valid_language_code
from app.services.file_parser import FileParser
import os
import tempfile
import yaml

translate_bp = Blueprint('translate', __name__)

# Initialize ModelService once per app
model_service = ModelService(Config())

@translate_bp.route('/translate', methods=['POST'])
def translate() -> tuple:
    try:
        if request.content_type and request.content_type.startswith('multipart/form-data'):
            file = request.files.get('file')
            translate_from = request.form.get('translate_from')
            translate_to = request.form.get('translate_to')
            export_format = request.form.get('export_format')
            if not file or not translate_from or not translate_to or not export_format:
                return jsonify({'error': 'Missing required fields'}), 400
            if not is_valid_language_code(translate_from) or not is_valid_language_code(translate_to):
                return jsonify({'error': 'Invalid language code'}), 400
            if export_format not in ['json', 'yaml']:
                return jsonify({'error': 'Invalid export format'}), 400
            # Save file to temp and read content
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                file.save(tmp)
                tmp_path = tmp.name
            with open(tmp_path, 'r', encoding='utf-8') as f:
                content = f.read()
            os.remove(tmp_path)
            # Stub: parse and process file
            parser = FileParser()
            if not parser.is_valid_format(content):
                return jsonify({'error': 'Invalid file format'}), 400
            # TODO: Extract, translate, reconstruct, and export
            return jsonify({'result': 'stubbed file translation'}), 200
        else:
            data = request.get_json()
            text = data.get('text')
            source_lang = data.get('source_lang')
            target_lang = data.get('target_lang')
            if not text or not source_lang or not target_lang:
                return jsonify({'error': 'Missing required fields'}), 400
            if not is_valid_language_code(source_lang) or not is_valid_language_code(target_lang):
                return jsonify({'error': 'Invalid language code'}), 400
            result = model_service.translate(text, source_lang, target_lang)
            return jsonify({'translation': result}), 200
    except Exception as e:
        # TODO: Add proper error handling/logging
        return jsonify({'error': 'Internal server error'}), 500

@translate_bp.route('/languages', methods=['GET'])
def list_languages() -> tuple:
    try:
        codes = get_supported_languages()
        languages = [{"code": code, "name": get_language_name(code)} for code in codes]
        return jsonify({"languages": languages}), 200
    except Exception as e:
        # TODO: Add proper error handling/logging
        return jsonify({"error": "Internal server error"}), 500 