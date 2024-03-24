"""Test the partition getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from tests.mock_storage_lib import mock_command_executor_method, mock_partitions_sda, mock_partitions_sda_entity, \
    mock_partitions_sdb, mock_partitions_sdb_entity
from storage_lib.managers.getters import PartitionGetter


class TestPartitionGetter(unittest.IsolatedAsyncioTestCase):
    """Test the partition getter."""

    def setUp(self) -> None:
        """Set up the test."""
        self.partition_getter = PartitionGetter(CommandManager("augusto", "augusto"))

    async def test_get_partitions_sda(self) -> None:
        """Test get the partitions of sda disk."""
        with mock.patch(mock_command_executor_method, return_value=mock_partitions_sda):
            self.assertEqual(await self.partition_getter.get_partitions("/dev/sda/"),
                             mock_partitions_sda_entity)

    async def test_get_partitions_sdb(self) -> None:
        """Test get the partitions of sdb disk."""
        with mock.patch(mock_command_executor_method, return_value=mock_partitions_sdb):
            self.assertEqual(await self.partition_getter.get_partitions("/dev/sdb/"),
                             mock_partitions_sdb_entity)
