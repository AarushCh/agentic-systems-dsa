import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.event_scheduler import can_attend_all, min_rooms_required  # type: ignore

class TestEventScheduler(unittest.TestCase):
    def test_can_attend_all(self):
        self.assertFalse(can_attend_all([(0, 30), (5, 10), (15, 20)]))
        self.assertTrue(can_attend_all([(9, 10), (10, 11), (11, 12)]))
        self.assertTrue(can_attend_all([]))

    def test_min_rooms_required(self):
        self.assertEqual(min_rooms_required([(0, 30), (5, 10), (15, 20)]), 2)
        self.assertEqual(min_rooms_required([(9, 10), (10, 11), (11, 12)]), 1)
        self.assertEqual(min_rooms_required([(1, 5), (8, 9), (2, 6), (4, 10)]), 3)

if __name__ == '__main__':
    unittest.main()