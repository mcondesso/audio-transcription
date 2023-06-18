import os
from src import create_app


def main():
    app = create_app()
    app.run(
        host=os.getenv("TRANSCRIPTION_SERVER_ADDRESS"),
        port=int(os.getenv("TRANSCRIPTION_SERVER_PORT")),
    )


if __name__ == "__main__":
    main()
