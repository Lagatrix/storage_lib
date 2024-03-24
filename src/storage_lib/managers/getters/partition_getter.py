"""Get partitions of the system."""
from shell_executor_lib import CommandManager

from storage_lib.entities import Partition


class PartitionGetter:
    """Get partitions of the system."""

    def __init__(self, command_manager: CommandManager):
        """Initialize the DiskGetter.

        Args:
            command_manager: To make commands in the shell.
        """
        self.__command_manager: CommandManager = command_manager

    async def get_partitions(self, disk_name: str) -> list[Partition]:
        """Get the partitions of the disk.

        Args:
            disk_name: The disk to get the partitions.

        Returns:
            The partitions of the disk

        Raises:
            CommandError: If the exit code is not 0.
        """
        disk_list: list[Partition] = []

        data_list: list[str] = (await self.__command_manager.execute_command(
            f"/bin/lsblk -p -b -n -l -o name,size,fstype,mountpoints,fsuse% {disk_name}", False))[1:]

        for data_row in data_list:
            data: list[str] = data_row.split()

            if len(data) < 2:
                disk_list[-1].mount_points.append(data[0])
            else:
                byte_size: int = int(data[1])
                type_format: str = data[2] if len(data) > 2 else "None"
                mount_point_list: list[str] = [data[3]] if len(data) > 3 else []
                use: str = data[4] if len(data) > 4 else "None"

                disk_list.append(Partition(data[0], type_format, byte_size, use, mount_point_list))

        return disk_list
