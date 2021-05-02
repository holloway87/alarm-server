import websockets


class CommandEvent:
    """
    Contains all available data for a command execution event.
    """
    message: str
    client: websockets.WebSocketServerProtocol

    def __init__(self, message: str, client: websockets.WebSocketServerProtocol):
        """
        Sets all needed data.

        :param message: web socket message
        :param client: web socket client connection
        """
        self.client = client
        self.message = message
