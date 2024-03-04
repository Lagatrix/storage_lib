"""Mocks of the partitions."""
from storage_lib.entities import Partition

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
        999727569920,
        "28%",
        ["/a", "/home/javier/1TB"]
    ),
    Partition(
        "/dev/sda2",
        "ntfs",
        575668224,
        "None",
        []
    )
]

mock_partitions_sdb_entity = [
    Partition(
        "/dev/sdb1",
        "ntfs",
        575668224,
        "None",
        []
    ),
    Partition(
        "/dev/sdb3",
        "None",
        1024,
        "None",
        []
    ),
    Partition(
        "/dev/sdb5",
        "swap",
        1023410176,
        "None",
        ["[SWAP]"]
    ),
    Partition(
        "/dev/sdb6",
        "ext4",
        267798970368,
        "50%",
        ["/"]
    )
]
