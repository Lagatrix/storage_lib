"""Test the disk manager."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from tests.mock_storage_lib import mock_command_executor_method, mock_disks, mock_disk_entity_with_partitions, \
    mock_partitions_sda, mock_partitions_sdb
from storage_lib import DiskManager


class TestDiskManager(unittest.IsolatedAsyncioTestCase):
    """Test the disk manager."""

    def setUp(self) -> None:
        """Set up the test."""
        self.disk_manager = DiskManager(CommandManager("augusto", "augusto"))

    async def test_get_disks(self) -> None:
        """Test get the disks."""
        with mock.patch(mock_command_executor_method, side_effect=(mock_disks, mock_partitions_sda,
                                                                   mock_partitions_sdb)):
            self.assertEqual(await self.disk_manager.get_disks(), mock_disk_entity_with_partitions)
