from flask import Flask, jsonify

def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "ok"}), 200

    return app
