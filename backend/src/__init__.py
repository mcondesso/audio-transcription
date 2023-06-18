"""This module is used to setup the Flask app."""
import os

from flask import Flask
from flask_cors import CORS

from src.log_config import configure_app_logging

from src.routes.root import root_bp
from src.routes.transcribe import transcribe_bp


def create_app():
    """Factory function to setup the Flask app"""
    app = Flask(__name__)

    configure_app_logging(app)

    app.secret_key = "foobar"
    CORS(app)

    app.config["FLASK_RUN_PORT"] = os.getenv("FLASK_RUN_PORT")

    app.register_blueprint(root_bp)
    app.register_blueprint(transcribe_bp)

    return app
