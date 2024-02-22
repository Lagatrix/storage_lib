"""This entity represents a disk."""
from dataclasses import dataclass

from storage_lib.entities.partition import Partition


@dataclass
class Disk:
    """This entity represents a disk.

    Attributes:
        name: The name of the disk.
        model: The model of the disk.
        size: The size of the disk.
        size_in_bytes: The size of the disk in bytes.
        partitions: The partitions that the disk contains.
    """
    name: str
    model: str
    size: str
    size_in_bytes: int
    partitions: list[Partition]
