"""This module sets up the /transcribe endpoint."""
import logging
from flask import Blueprint, request, jsonify

from src.services.transcription_service import audio_transcriber


transcribe_bp = Blueprint("transcribe_bp", __name__)
transcribe_logger = logging.getLogger("backend.routes.transcribe_logger")


@transcribe_bp.route("/transcribe", methods=["POST"])
def transcribe():
    # Validate the request content-type header
    if request.content_type != "audio/wav":
        message = "Invalid content type"
        transcribe_logger.warning(message)
        return jsonify({"transcription": "", "message": message}), 400

    # Get the data from the request
    audio_data = request.get_data()

    # Validate the content of the request
    if not audio_data:
        message = "The request data was empty"
        transcribe_logger.warning(message)
        return jsonify({"transcription": "", "message": message}), 400

    # Transcribe the audio data
    transcription = audio_transcriber.get_transcription(audio_data)

    return jsonify({"transcription": transcription, "message": "Success"}), 200
