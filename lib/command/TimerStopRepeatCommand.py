import re

from lib.CommandEvent import CommandEvent
from lib.TimerHandler import TimerHandler
from lib.command.AbstractCommand import AbstractCommand


class TimerStopRepeatCommand(AbstractCommand):
    """
    Command to stop a repeated timer.
    """
    timer_handler: TimerHandler

    def __init__(self, timer_handler: TimerHandler):
        """
        Set all needed services.

        :param timer_handler: handler for alarms
        """
        self.timer_handler = timer_handler

    async def execute(self, event: CommandEvent) -> None:
        self.timer_handler.stop_timer(re.sub(r'^timer_stop_repeat', 'timer_repeat', event.message))
