"""Test the size utils."""
import unittest

from storage_lib.utils import bytes_to_understandable_sizes, percentage_of_size_partition_in_disk


class TestSizeUtils(unittest.TestCase):
    """Test the size utils."""

    def test_bytes_to_understandable_sizes(self) -> None:
        """Test bytes to understandable sizes."""
        self.assertEqual(bytes_to_understandable_sizes(0), "0.00 B")
        self.assertEqual(bytes_to_understandable_sizes(1000), "1000.00 B")
        self.assertEqual(bytes_to_understandable_sizes(1024), "1.00 KB")
        self.assertEqual(bytes_to_understandable_sizes(1048576), "1.00 MB")
        self.assertEqual(bytes_to_understandable_sizes(1073741824), "1.00 GB")
        self.assertEqual(bytes_to_understandable_sizes(1099511627776), "1.00 TB")
        self.assertEqual(bytes_to_understandable_sizes(1125899906842624), "1.00 PB")
        self.assertEqual(bytes_to_understandable_sizes(1152921504606846976), "1.00 EB")
        self.assertEqual(bytes_to_understandable_sizes(1180591620717411303424), "1.00 ZB")
        self.assertEqual(bytes_to_understandable_sizes(1208925819614629174706176), "1.00 YB")
        self.assertEqual(bytes_to_understandable_sizes(1000 * (3**80)), "119399021538774.06 YB")
        self.assertEqual(bytes_to_understandable_sizes(1000204886016), "931.51 GB")

    def test_percentage_of_size_partition_in_disk(self) -> None:
        """Test percentage of size partition in disk."""
        self.assertEqual(percentage_of_size_partition_in_disk(1000, 1000), "100.00%")
        self.assertEqual(percentage_of_size_partition_in_disk(1000, 10000), "10.00%")
        self.assertEqual(percentage_of_size_partition_in_disk(1000, 100000), "1.00%")
        self.assertEqual(percentage_of_size_partition_in_disk(1000, 1000000), "0.10%")
        self.assertEqual(percentage_of_size_partition_in_disk(1000, 10000000), "0.01%")
        self.assertEqual(percentage_of_size_partition_in_disk(1000, 100000000), "0.00%")
