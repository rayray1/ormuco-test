import unittest
from overlap import check_overlap


class TestOverlap(unittest.TestCase):
    """Test if two lines overlap or not."""
    def test_overlap(self):
        line1 = (1, 5)
        line2 = (2, 6)
        line3 = (6, 8)
        self.assertTrue(check_overlap(line1, line2))
        self.assertFalse(check_overlap(line1, line3))


if __name__ == '__main__':
    unittest.main()
