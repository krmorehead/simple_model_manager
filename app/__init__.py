from flask import Flask, jsonify

def create_app() -> Flask:
    app = Flask(__name__)

    from app.routes.translate import translate_bp
    app.register_blueprint(translate_bp)

    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "ok"}), 200

    return app
