from datetime import datetime, timedelta

from lib.AbstractAlarmData import AbstractAlarmData


class AlarmDataRelative(AbstractAlarmData):
    """
    Alarm data for a relative time.
    """
    amount: int
    unit: str

    def __init__(self, amount: int, unit: str):
        """
        Sets amount and time unit for the relative time.

        :param amount: amount of the given unit
        :param unit: s = seconds | m = minutes | h = hours
        """
        self.amount = amount
        self.unit = unit

    def get_list_data(self) -> str:
        return '%d%s' % (self.amount, self.unit)

    def get_next_date(self) -> datetime:
        seconds = self.amount
        if 'm' == self.unit:
            seconds *= 60
        elif 'h' == self.unit:
            seconds *= 3600
        delta = timedelta(seconds=seconds)

        return datetime.now() + delta
