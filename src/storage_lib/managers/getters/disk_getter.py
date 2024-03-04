"""Get disks of the system."""
import re
from typing import AsyncIterable

from shell_executor_lib import CommandManager

from storage_lib.entities import Disk


class DiskGetter:
    """Get disks of the system."""

    def __init__(self, command_manager: CommandManager):
        """Initialize the DiskGetter.

        Args:
            command_manager: To make commands in the shell.
        """
        self.__command_manager: CommandManager = command_manager

    async def get_disks(self) -> AsyncIterable[Disk]:
        """Get the disks of the system without partitions.

        Returns:
            The disks of the system without partitions.

        Raises:
            CommandError: If the exit code is not 0.
        """
        data_list: list[str] = await self.__command_manager.execute_command(
            "/bin/lsblk -p -b -d -l -n -o name,size,model", False)

        for data_row in data_list:
            data: list[str] = re.sub(r'\s', ':', re.sub(r'\s+', " ", data_row), 2).split(":")

            byte_size: int = int(data[1])

            yield Disk(data[0], data[2], byte_size, [])
