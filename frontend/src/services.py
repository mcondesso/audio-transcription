import logging
import os
import requests

logger = logging.getLogger(__name__)


def request_transcription(audio_file):
    logger.info("Requesting transcription")

    # Open the WAV file and read the contents as binary data
    with open(audio_file, "rb") as f:
        audio_data = f.read()

    # Set the HTTP headers
    headers = {"Content-Type": "audio/wav"}

    # Send the HTTP request with the audio data as the body
    response = requests.post(url=get_url(), headers=headers, data=audio_data)

    if response.ok:
        response_json = response.json()
        transcription = response_json["transcription"]
        return transcription
    else:
        # raise Exception(response.status_code)
        logger.error(f"Request failed with status code {response.status_code}")
        return None


def get_url():
    address = "http://" + os.getenv("TRANSCRIPTION_SERVER_ADDRESS")
    port = os.getenv("TRANSCRIPTION_SERVER_PORT")
    route = os.getenv("TRANSCRIPTION_SERVER_ROUTE")
    return f"{address}:{port}/{route}"
