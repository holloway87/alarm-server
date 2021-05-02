import re

from lib.AlarmData import AlarmData
from lib.AlarmDataFixed import AlarmDataFixed
from lib.AlarmDataRelative import AlarmDataRelative
from lib.CommandEvent import CommandEvent
from lib.TimerHandler import TimerHandler
from lib.command.AbstractCommand import AbstractCommand


class TimerRepeatCommand(AbstractCommand):
    """
    Command to add a new repeated timer.
    """
    timer_handler: TimerHandler

    def __init__(self, timer_handler: TimerHandler):
        """
        Set all needed services.

        :param timer_handler: handler for alarms
        """
        self.timer_handler = timer_handler

    async def execute(self, event: CommandEvent) -> None:
        timer_match = re.match(r'timer_repeat (\d{1,2}):(\d{1,2})', event.message)
        if timer_match:
            data = AlarmData(AlarmDataFixed(int(timer_match.group(1)), int(timer_match.group(2))),
                             repeated=True)
            self.timer_handler.add_timer(event.message, data)
        else:
            timer_match = re.match(r'timer_repeat (\d+)([smh])', event.message)
            if timer_match:
                data = AlarmData(AlarmDataRelative(int(timer_match.group(1)), timer_match.group(2)),
                                 repeated=True)
                self.timer_handler.add_timer(event.message, data)
