"""Mocks of the disks."""
from tests.mock_storage_lib.mock_partition_manager import mock_partitions_sda_entity, mock_partitions_sdb_entity
from storage_lib.entities.disk import Disk

mock_disks = ["/dev/sda  1000204886016 KINGSTON SA400S37480G", "/dev/sdb 480103981056 ST1000DM010-2EP102"]

mock_disk_entity_without_partitions = [
    Disk(
        "/dev/sda",
        "KINGSTON SA400S37480G",
        1000204886016,
        []
    ),
    Disk(
        "/dev/sdb",
        "ST1000DM010-2EP102",
        480103981056,
        []
    )
]

mock_disk_entity_with_partitions = [
    Disk(
        "/dev/sda",
        "KINGSTON SA400S37480G",
        1000204886016,
        mock_partitions_sda_entity
    ),
    Disk(
        "/dev/sdb",
        "ST1000DM010-2EP102",
        480103981056,
        mock_partitions_sdb_entity
    )
]
