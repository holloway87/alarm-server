from lib.CommandEvent import CommandEvent


class AbstractCommand:
    """
    Abstract command, interface for command implementations.
    """
    async def execute(self, event: CommandEvent) -> None:
        """
        Executes the command.

        :param event: containing all data
        :return:
        """
        raise NotImplementedError()
