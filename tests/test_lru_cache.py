import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.lru_cache import LRUCache  # type: ignore

class TestLRUCache(unittest.TestCase):
    def test_cache_operations(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)    
        cache.put(3, 3)                      
        self.assertEqual(cache.get(2), -1)   
        cache.put(4, 4)                      
        self.assertEqual(cache.get(1), -1)   
        self.assertEqual(cache.get(3), 3)    
        self.assertEqual(cache.get(4), 4)    

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(1, 20)
        self.assertEqual(cache.get(1), 20)

if __name__ == '__main__':
    unittest.main()