from lib.CommandEvent import CommandEvent
from lib.TimerHandler import TimerHandler
from lib.command.AbstractCommand import AbstractCommand


class ListCommand(AbstractCommand):
    """
    Command to return the list of all alarms.
    """
    timer_handler: TimerHandler

    def __init__(self, timer_handler: TimerHandler):
        """
        Set all needed services.

        :param timer_handler:
        """
        self.timer_handler = timer_handler

    async def execute(self, event: CommandEvent) -> None:
        alarm_list = ''
        for timer in self.timer_handler.timers:
            if alarm_list:
                alarm_list += "\n"
            alarm_list += self.timer_handler.timers[timer].get_list_data()
            if timer in self.timer_handler.active_timers:
                alarm_list += ';%s' % self.timer_handler.active_timers[timer].strftime('%Y-%m-%d %H:%M:%S')

        await event.client.send(alarm_list)
