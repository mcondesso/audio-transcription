import io
import json
import logging

import speech_recognition


transcription_logger = logging.getLogger("backend.transcription_logger")


class AudioTranscriberException(Exception):
    """Exceptions thrown by the AudioTranscriber"""


class AudioTranscriber:
    def __init__(self):
        transcription_logger.info("Loading the model")
        self.model = speech_recognition.Recognizer()

def get_transcription(self, audio_data):
    # Create a byte stream from the audio data
    audio_stream = io.BytesIO(audio_data)

    # Create an AudioFile object from the byte stream
    with speech_recognition.AudioFile(audio_stream) as source:
        # Convert the AudioFile into an AudioData object
        audio = self.model.record(source)

    # Transcribe the audio
    vosk_response = self.model.recognize_vosk(audio)

    # Extract the text from the vosk response
    transcription = json.loads(vosk_response)["text"]

    # Debug log
    transcription_logger.info(transcription)

    return transcription


audio_transcriber = AudioTranscriber()
