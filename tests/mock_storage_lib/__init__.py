"""Exposed mock_storage_lib classes and methods."""
from tests.mock_storage_lib.mock_partition_manager import (mock_partitions_sda, mock_partitions_sdb,
                                                           mock_partitions_sda_entity, mock_partitions_sdb_entity)
from tests.mock_storage_lib.mock_disk_manager import (mock_disks, mock_disk_entity_without_partitions,
                                                      mock_disk_entity_with_partitions)

mock_command_executor_method = "shell_executor_lib.CommandManager.execute_command"
