from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import requests

splash_bp = Blueprint('splash', __name__)

@splash_bp.route('/', methods=['GET'])
def root():
    return redirect(url_for('splash.splash'))

@splash_bp.route('/splash', methods=['GET'])
def splash():
    return render_template('splash.html')

@splash_bp.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    yaml_text = data.get('yaml')
    language = data.get('language')
    # Send to /translate endpoint (simulate as if from client)
    # For now, use requests to call local API (could refactor to call service directly)
    resp = requests.post('http://localhost:5000/translate', json={
        'text': yaml_text,
        'source_lang': 'en',
        'target_lang': language
    })
    return jsonify(resp.json()), resp.status_code 