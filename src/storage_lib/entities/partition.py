"""This entity represents a partition."""
from dataclasses import dataclass


@dataclass
class Partition:
    """This entity represents a partition.

    Attributes:
        name: The name of the partition.
        type_format: The type format of the partition.
        size_in_bytes: The size of the partition in bytes.
        use: The use in disk of the partition.
        mount_points: The mount points of the partition.
    """
    name: str
    type_format: str
    size_in_bytes: int
    use: str
    mount_points: list[str]
