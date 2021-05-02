import re

from lib.CommandEvent import CommandEvent
from lib.TimerHandler import TimerHandler
from lib.command.AbstractCommand import AbstractCommand


class TimerStopCommand(AbstractCommand):
    """
    Command to stop a timer.
    """
    timer_handler: TimerHandler

    def __init__(self, timer_handler: TimerHandler):
        """
        Sets all needed services.

        :param timer_handler: handler for alarms
        """
        self.timer_handler = timer_handler

    async def execute(self, event: CommandEvent) -> None:
        self.timer_handler.stop_timer(re.sub(r'^timer_stop', 'timer', event.message))
