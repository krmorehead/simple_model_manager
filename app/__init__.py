from flask import Flask, jsonify, request
import logging
from config.settings import Config

def create_app() -> Flask:
    app = Flask(__name__)

    # Structured logging setup
    log_level = getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO)
    logging.basicConfig(level=log_level, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    app.logger.setLevel(log_level)

    from app.routes.translate import translate_bp
    app.register_blueprint(translate_bp, url_prefix='/api')

    from app.routes.splash import splash_bp
    app.register_blueprint(splash_bp)

    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "ok"}), 200

    @app.errorhandler(400)
    def bad_request(error):
        app.logger.warning(f"400 Bad Request: {request.url} - {error}")
        return jsonify({"error": "Bad Request", "message": str(error)}), 400

    @app.errorhandler(404)
    def not_found(error):
        app.logger.warning(f"404 Not Found: {request.url} - {error}")
        return jsonify({"error": "Not Found", "message": str(error)}), 404

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f"500 Internal Server Error: {request.url} - {error}")
        return jsonify({"error": "Internal Server Error", "message": str(error)}), 500

    return app
