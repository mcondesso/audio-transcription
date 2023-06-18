"""This module is used to configure logging for the backend.

"""

import logging
import os
from logging.config import dictConfig

from flask import request


# Logging configuration
dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "%(asctime)s %(levelname)s: %(message)s",
            },
        },
        "handlers": {
            "file": {
                # if needed, switch to RotatingFileHandler or TimeRotatingFileHandler
                "class": "logging.FileHandler",
                "filename": os.path.join(os.getenv("LOG_FOLDER"), os.getenv("LOG_FILENAME")),
                "formatter": "default",
            },
        },
        "loggers": {
            "backend": {"handlers": ["file"], "level": "INFO"},
        },
    },
)


def configure_app_logging(app):
    """Function to setup logging for all app routes."""

    # Set this logger as a child of backend logger to inherit its settings
    request_logger = logging.getLogger("backend.request_logger")

    # Get logger with appropriate level, according to status code of the server response
    def get_response_logger(status):
        if status.startswith("4"):
            # Client error responses
            return request_logger.warning
        elif status.startswith("5"):
            # Server error responses
            return request_logger.error
        else:
            return request_logger.info

    # Setup logging for each incoming request
    @app.before_request
    def before_request():
        """Logging every request that comes in."""
        request_logger.info(
            "route %s %s %s - from %s",
            request.path,
            request.method,
            request.environ.get("SERVER_PROTOCOL"),
            request.remote_addr,
        )

    # Setup logging for each outgoing response
    @app.after_request
    def after_request(response):
        """Logging the response to every request."""
        log = get_response_logger(response.status)
        log(
            "route %s %s %s - from %s - %s",
            request.path,
            request.method,
            request.environ.get("SERVER_PROTOCOL"),
            request.remote_addr,
            response.status,
        )

        return response
