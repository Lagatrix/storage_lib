"""Mocks of the partitions."""
from storage_lib.entities import Partition
from storage_lib.utils.size_utils import bytes_to_understandable_sizes, percentage_of_size_partition_in_disk

mock_partitions_sda = ["/dev/sda  1000204886016",
                       "/dev/sda1  999727569920 ext4   /a                  28%",
                       "                               /home/javier/1TB",
                       "/dev/sda2    575668224 ntfs"]

mock_partitions_sdb = ["/dev/sdb  480103981056",
                       "/dev/sdb1    575668224 ntfs",
                       "/dev/sdb3         1024",
                       "/dev/sdb5   1023410176 swap   [SWAP]",
                       "/dev/sdb6 267798970368 ext4   /              50%"]

mock_partitions_sda_entity = [
    Partition(
        "/dev/sda1",
        "ext4",
        bytes_to_understandable_sizes(999727569920),
        999727569920,
        "28%",
        percentage_of_size_partition_in_disk(999727569920, 1000204886016),
        ["/a", "/home/javier/1TB"]
    ),
    Partition(
        "/dev/sda2",
        "ntfs",
        bytes_to_understandable_sizes(575668224),
        575668224,
        "None",
        percentage_of_size_partition_in_disk(575668224, 1000204886016),
        []
    )
]

mock_partitions_sdb_entity = [
    Partition(
        "/dev/sdb1",
        "ntfs",
        bytes_to_understandable_sizes(575668224),
        575668224,
        "None",
        percentage_of_size_partition_in_disk(575668224, 480103981056),
        []
    ),
    Partition(
        "/dev/sdb3",
        "None",
        bytes_to_understandable_sizes(1024),
        1024,
        "None",
        percentage_of_size_partition_in_disk(1024, 480103981056),
        []
    ),
    Partition(
        "/dev/sdb5",
        "swap",
        bytes_to_understandable_sizes(1023410176),
        1023410176,
        "None",
        percentage_of_size_partition_in_disk(1023410176, 480103981056),
        ["[SWAP]"]
    ),
    Partition(
        "/dev/sdb6",
        "ext4",
        bytes_to_understandable_sizes(267798970368),
        267798970368,
        "50%",
        percentage_of_size_partition_in_disk(267798970368, 480103981056),
        ["/"]
    )
]
