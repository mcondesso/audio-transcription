import logging
import os
from dotenv import load_dotenv

from gradio import Audio, Textbox, Interface

from src.services import request_transcription


logging.config.fileConfig("logging.conf")

logger = logging.getLogger(__name__)


def create_interface():
    logger.info("Booting the app")

    load_dotenv()

    print("\n-----------------------")
    print(os.getenv("TRANSCRIPTION_SERVER_PORT"))
    print(os.getenv("TRANSCRIPTION_SERVER_ROUTE"))
    print("-----------------------\n\n")
    import sys

    sys.exit(0)

    audio_input = Audio(source="upload", type="filepath")
    output_text = Textbox()

    interface = Interface(
        fn=request_transcription,
        inputs=audio_input,
        outputs=output_text,
        title="Audio Transcription",
        description="Upload an audio file and submit",
    )

    return interface
