import websockets

from lib.CommandEvent import CommandEvent
from lib.command.AbstractCommand import AbstractCommand


class CommandHandler:
    """
    Handles all commands when something was received from a web socket client.
    """
    commands: dict[str, AbstractCommand]

    def __init__(self):
        """
        Creates all instances.
        """
        self.commands = {}

    def add_command(self, key: str, command: AbstractCommand) -> None:
        """
        Adds a command.

        :param key: unique command key, is the first word in the web socket message
        :param command: command instance
        :return:
        """
        self.commands[key] = command

    async def handle_command(self, message: str, web_socket: websockets.WebSocketServerProtocol) -> None:
        """
        Checks if the message contains a known command and executes it with the whole web socket message.

        :param message: web socket message
        :param web_socket: web socket client connection
        :return:
        """
        command_name = message
        idx = message.find(' ')
        if 0 <= idx:
            command_name = message[0:idx]
        for key, command in self.commands.items():
            if key == command_name:
                await command.execute(CommandEvent(message, web_socket))
                break
