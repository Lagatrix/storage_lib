"""Test the disk getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from tests.mock_storage_lib import mock_command_executor_method, mock_disks, mock_disk_entity_without_partitions
from storage_lib.managers.getters import DiskGetter


class TestDiskGetter(unittest.IsolatedAsyncioTestCase):
    """Test the disk getter."""

    def setUp(self) -> None:
        """Set up the test."""
        self.disk_getter = DiskGetter(CommandManager("augusto", "augusto"))

    async def test_get_disks(self) -> None:
        """Test get the disks."""
        with mock.patch(mock_command_executor_method, return_value=mock_disks):
            self.assertEqual([disk async for disk in self.disk_getter.get_disks()], mock_disk_entity_without_partitions)
