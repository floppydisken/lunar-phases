from django.test import TestCase
from datetime import datetime

from .lunar import LunarPhase, LunarPhases, in_range
from .utils import map_range, clamp


class UtilTests(TestCase):
    def test_clamp(self):
        self.assertEqual(clamp(1.2, 0, 1), 1)
        self.assertEqual(clamp(0.9, 0, 1), 0.9)
        self.assertEqual(clamp(-0.1, 0, 1), 0)
        self.assertEqual(clamp(0.1, 0, 1), 0.1)

    def test_map_range(self):
        self.assertEqual(map_range(180, 0, 360, 0, 1), 0.5)
        self.assertEqual(map_range(-1, 0, 360, 0, 1), 0)
        self.assertEqual(map_range(361, 0, 360, 0, 1), 1)


class InRangeTests(TestCase):
    def test_flipped_values(self):
        self.assertFalse(in_range(0.25, [0.9, 0.1]))
        self.assertTrue(in_range(0.91, [0.9, 0.1]))
        self.assertTrue(in_range(0.09, [0.9, 0.1]))

    def test_regular_values(self):
        self.assertTrue(in_range(0.24, [0.23, 0.25]))
        self.assertFalse(in_range(0.22, [0.23, 0.25]))
