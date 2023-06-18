import os

from src import create_interface


def main():
    interface = create_interface()

    interface.launch(
        server_name=os.getenv("APP_SERVER_ADDRESS"),
        server_port=int(os.getenv("APP_SERVER_PORT")),
    )


if __name__ == "__main__":
    main()
