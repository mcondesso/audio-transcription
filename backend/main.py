import os
import base64
import io
import json
import logging
import logging.config
import speech_recognition
from flask import Flask, jsonify, request


logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


app = Flask(__name__)
model = None


def decode_audio(encoded_audio):
    return base64.b64decode(encoded_audio)


def load_model():
    logger.info("Loading the model")
    global model
    model = speech_recognition.Recognizer()


def get_transcription(audio_data):
    # Create a byte stream from the audio data
    audio_stream = io.BytesIO(audio_data)

    # Create an AudioFile object from the byte stream
    with speech_recognition.AudioFile(audio_stream) as source:
        # Convert the AudioFile into an AudioData object
        audio = model.record(source)

    # Transcribe the audio
    vosk_response = model.recognize_vosk(audio)

    # Extract the text from the vosk response
    transcription = json.loads(vosk_response)["text"]

    return transcription


@app.route("/", methods=["GET"])
def index():
    logger.info("Received a ping")
    return "Server is online\n"


import pdb

pdb.set_trace()


@app.route("/" + os.getenv("TRANSCRIPTION_SERVER_ROUTE"), methods=["POST"])
def transcribe():
    logger.info("Received a transcription request")

    if request.content_type != "audio/wav":
        return "Invalid content type", 400

    audio_data = request.get_data()

    transcription = get_transcription(audio_data)

    logger.info(transcription)

    return jsonify({"transcription": transcription})


def main():
    logger.info("Booting the server")

    load_model()
    app.run(
        host=os.getenv("TRANSCRIPTION_SERVER_ADDRESS"),
        port=int(os.getenv("TRANSCRIPTION_SERVER_PORT")),
    )


if __name__ == "__main__":
    main()
