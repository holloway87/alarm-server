from datetime import datetime, timedelta

from lib.AbstractAlarmData import AbstractAlarmData


class AlarmDataFixed(AbstractAlarmData):
    """
    Alarm data for a fixed time.
    """
    hours: int
    minutes: int

    def __init__(self, hours: int, minutes: int):
        """
        Sets hours and minutes of the time for the alarm.

        :param hours: hours part of the time
        :param minutes: minutes part of the time
        """
        self.hours = hours
        self.minutes = minutes

    def get_list_data(self) -> str:
        return '%d:%02d' % (self.hours, self.minutes)

    def get_next_date(self) -> datetime:
        datetime_now = datetime.now()
        datetime_alarm = datetime(year=datetime_now.year, month=datetime_now.month, day=datetime_now.day,
                                  hour=self.hours, minute=self.minutes)
        if datetime_now.time() >= datetime_alarm.time():
            datetime_alarm += timedelta(days=1)

        return datetime_alarm
