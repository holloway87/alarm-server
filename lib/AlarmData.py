from lib.AbstractAlarmData import AbstractAlarmData


class AlarmData:
    """
    Contains all data for an alarm.
    """
    data: AbstractAlarmData
    repeated: bool

    def __init__(self, data: AbstractAlarmData, repeated: bool):
        """
        Set all data.

        :param data: timer data depending on the type
        :param repeated: if the timer will be repeated
        """
        self.data = data
        self.repeated = repeated

    def get_list_data(self):
        """
        Returns the data representation of the timer, will be used to send it over the web socket.

        :return:
        """
        key = 'timer'
        if self.repeated:
            key += '_repeat'
        return '%s %s' % (key, self.data.get_list_data())
