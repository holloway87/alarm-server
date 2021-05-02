import asyncio
import websockets

from lib.AlarmPlayer import AlarmPlayer
from lib.CommandHandler import CommandHandler
from lib.TimerHandler import TimerHandler
from lib.command.ListCommand import ListCommand
from lib.command.PlayCommand import PlayCommand
from lib.command.StopCommand import StopCommand
from lib.command.TimerCommand import TimerCommand
from lib.command.TimerRepeatCommand import TimerRepeatCommand
from lib.command.TimerStopCommand import TimerStopCommand
from lib.command.TimerStopRepeatCommand import TimerStopRepeatCommand


class AlarmServer:
    """
    Main entry point for for the server.

    Manages connections with clients and handles all alarms.
    """
    alarm_player: AlarmPlayer
    command_handler: CommandHandler
    timer_handler: TimerHandler

    def __init__(self, sound_file: str) -> None:
        """
        Creates all needed instances.

        :param sound_file: absolute path for the alarm sound file
        """
        self.alarm_player = AlarmPlayer(sound_file)
        self.command_handler = CommandHandler()
        self.timer_handler = TimerHandler(self.alarm_player)
        self.init_commands()

    # noinspection PyUnusedLocal
    async def handle_socket_client(self, web_socket: websockets.WebSocketServerProtocol, path: str):
        """
        Handles a client from the web socket server.

        :param web_socket: client connection
        :param path: not used
        :return:
        """
        try:
            async for message in web_socket:
                await self.command_handler.handle_command(message, web_socket)
        except websockets.exceptions.ConnectionClosedError:
            pass
        finally:
            pass

    def init_commands(self):
        """
        Initializes all needed commands.

        :return:
        """
        self.command_handler.add_command('list', ListCommand(self.timer_handler))
        self.command_handler.add_command('play', PlayCommand(self.alarm_player))
        self.command_handler.add_command('stop', StopCommand(self.alarm_player))
        self.command_handler.add_command('timer', TimerCommand(self.timer_handler))
        self.command_handler.add_command('timer_repeat', TimerRepeatCommand(self.timer_handler))
        self.command_handler.add_command('timer_stop', TimerStopCommand(self.timer_handler))
        self.command_handler.add_command('timer_stop_repeat', TimerStopRepeatCommand(self.timer_handler))

    async def loop(self) -> None:
        """
        Loops for the alarm logic.

        :return:
        """
        while True:
            await asyncio.sleep(0.5)
            self.timer_handler.check_for_alarm()
