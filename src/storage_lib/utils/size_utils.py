"""This functions obtains information about sizes of partitions and disks."""


def bytes_to_understandable_sizes(bytes_size: float) -> str:
    """Transform bytes to understandable sizes.

    Args:
        bytes_size: The bytes size of partition or disk.

    Returns:
        The understandable size.
    """
    units_list = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

    for unit_list in units_list:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit_list}"
        bytes_size /= 1024

    return f"{bytes_size:.2f} {units_list[-1]}"


def percentage_of_size_partition_in_disk(partition_size: int, disk_size: int) -> str:
    """Calculate the percentage of partition size in disk size.

    Args:
        partition_size: The size of partition.
        disk_size: The size of disk.

    Returns:
        The percentage of partition size in disk size.
    """
    return f"{(partition_size / disk_size) * 100:.2f}%"
