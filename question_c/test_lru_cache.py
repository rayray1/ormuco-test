import unittest
import time
from lru_cache import Cache


class TestLruCache(unittest.TestCase):
    """ Test Lru Cache"""
    def test_lru_cache(self):
        cache = Cache(max_capacity=5)
        cache['c'] = 1
        self.assertEqual(cache['c'], 1)

    def test_lru_expiration(self):
        cache = Cache(max_capacity=4, expiration=5)
        cache['c'] = 1
        time.sleep(3)
        self.assertEqual(cache['a'], None)


if __name__ == '__main__':
    unittest.main()
