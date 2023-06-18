"""This module sets up the root endpoint."""
from flask import Blueprint

root_bp = Blueprint("root_bp", __name__)


@root_bp.route("/", methods=["GET"])
def index():
    return "Server is online.\n", 200
