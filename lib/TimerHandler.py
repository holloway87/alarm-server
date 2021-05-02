from datetime import datetime

from lib.AlarmData import AlarmData
from lib.AlarmPlayer import AlarmPlayer


class TimerHandler:
    """
    Handles all timers.
    """
    alarm_player: AlarmPlayer
    active_timers: dict[str, datetime]
    timers: dict[str, AlarmData]

    def __init__(self, alarm_player: AlarmPlayer):
        """
        Sets all default values.
        """
        self.alarm_player = alarm_player
        self.active_timers = {}
        self.timers = {}

    def add_timer(self, key: str, alarm_data: AlarmData) -> None:
        """
        Adds a new timer.

        :param key: unique key to stop it later
        :param alarm_data: contains all data for the timer
        :return:
        """
        self.timers[key] = alarm_data
        self.active_timers[key] = alarm_data.data.get_next_date()

    def check_for_alarm(self) -> None:
        """
        Checks if an alarm is ready to fire.

        :return:
        """
        for key, date in self.active_timers.items():
            now = datetime.now()
            if date.year == now.year and date.month == now.month and date.day == now.day and date.hour == now.hour and \
                    date.minute == now.minute and date.second == now.second:
                self.alarm_player.play()
                del self.active_timers[key]

                if key in self.timers:
                    if self.timers[key].repeated:
                        self.active_timers[key] = self.timers[key].data.get_next_date()
                    else:
                        del self.timers[key]

                break

    def stop_timer(self, key: str):
        """
        Stops the timer for the given key.

        :param key: timer key with which it was added
        :return:
        """
        if key in self.active_timers:
            del self.active_timers[key]

        if key in self.timers:
            del self.timers[key]
