from lib.AlarmPlayer import AlarmPlayer
from lib.CommandEvent import CommandEvent
from lib.command.AbstractCommand import AbstractCommand


class StopCommand(AbstractCommand):
    """
    Command to stop the alarm sound.
    """
    alarm_player: AlarmPlayer

    def __init__(self, alarm_player: AlarmPlayer):
        """
        Sets all needed services.

        :param alarm_player: Alarm player
        """
        self.alarm_player = alarm_player

    async def execute(self, event: CommandEvent) -> None:
        self.alarm_player.stop()
