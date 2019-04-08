import unittest
from version import compare_versions


class TestVersionString(unittest.TestCase):
    """Test if a given version string is greater than, equal,
        or less than the other."""

    def test_two_version_strings(self):
        version_a = "1.1"
        version_b = "1.2"
        self.assertTrue(compare_versions(version_a, version_b))

    def test_boolean(self):
        version_a = False
        version_b = "1.1"
        self.assertFalse(compare_versions(version_a, version_b))

    def test_string(self):
        version_a = "some_string"
        version_b = "25"
        self.assertFalse(compare_versions(version_a, version_b))

    def test_fraction(self):
        version_a = "1/2"
        version_b = "3/4"
        self.assertTrue(compare_versions(version_a, version_b))

    def test_integer(self):
        version_a = "2"
        version_b = "25"
        self.assertTrue(compare_versions(version_a, version_b))


if __name__ == '__main__':
    unittest.main()
