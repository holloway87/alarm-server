from datetime import datetime


class AbstractAlarmData:
    """
    Abstract class for alarm data.
    """
    def get_next_date(self) -> datetime:
        """
        Returns the datetime for the next alarm.

        :return:
        """
        raise NotImplementedError()

    def get_list_data(self) -> str:
        """
        Returns a representation of the timer data, will be used to send it over the web socket.

        :return:
        """
        raise NotImplementedError()
