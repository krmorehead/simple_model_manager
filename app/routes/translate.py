from flask import Blueprint, request, jsonify, current_app
from app.services.model_service import ModelService
from config.settings import Config

translate_bp = Blueprint('translate', __name__)

# Initialize ModelService once per app
model_service = ModelService(Config())

@translate_bp.route('/translate', methods=['POST'])
def translate() -> tuple:
    try:
        data = request.get_json()
        text = data['text']
        source_lang = data['source_lang']
        target_lang = data['target_lang']
        result = model_service.translate(text, source_lang, target_lang)
        return jsonify({'translation': result}), 200
    except KeyError as e:
        # TODO: Add proper error handling/logging
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        # TODO: Add proper error handling/logging
        return jsonify({'error': 'Internal server error'}), 500 