"""Manage disks of unix system."""
from shell_executor_lib import CommandManager

from storage_lib import Disk
from storage_lib.managers.getters import DiskGetter, PartitionGetter


class DiskManager:
    """Manage disks of unix system."""
    def __init__(self, command_manager: CommandManager) -> None:
        """Initialize the DiskManager."""
        self.__disk_getter: DiskGetter = DiskGetter(command_manager)
        self.__partition_getter: PartitionGetter = PartitionGetter(command_manager)

    async def get_disks(self) -> list[Disk]:
        """Get the disks of the system without partitions.

        Returns:
            Disk list of the system with partitions.
        """
        disk_list: list[Disk] = []

        async for disk in self.__disk_getter.get_disks():
            disk.partitions = await self.__partition_getter.get_partitions(disk.name, disk.size_in_bytes)
            disk_list.append(disk)

        return disk_list
