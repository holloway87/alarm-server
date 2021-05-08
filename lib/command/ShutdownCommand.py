from subprocess import run

from lib.CommandEvent import CommandEvent
from lib.command.AbstractCommand import AbstractCommand


class ShutdownCommand(AbstractCommand):
    """
    Command to shut down the machine.
    """
    async def execute(self, event: CommandEvent) -> None:
        run('poweroff')
