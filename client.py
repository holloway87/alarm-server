import argparse
import asyncio
import websockets


class AlarmClient:
    message: str

    def __init__(self, message: str):
        self.message = message

    async def web_socket_client(self):
        async with websockets.connect('ws://127.0.0.1:12614') as web_socket:
            await web_socket.send(self.message)


def main():
    parser = argparse.ArgumentParser(description='Send a message to the alarm server')
    parser.add_argument('message', metavar='MSG', type=str, help='Message for the server')
    arguments = parser.parse_args()

    client = AlarmClient(arguments.message)
    asyncio.get_event_loop().run_until_complete(client.web_socket_client())


if __name__ == '__main__':
    main()
