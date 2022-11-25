from django.test import TestCase
from datetime import datetime

from .lunar import LunarPhase, LunarPhases
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


class LunarPhasesTests(TestCase):
    def test_phase_should_be_new_moon(self):
        date = datetime(2022, 11, 24)
        phase = LunarPhase(date)

        self.assertEqual(LunarPhases.NEW_MOON, phase.phase)

    def test_phase_should_be_full_moon(self):
        date = datetime(2022, 12, 30)
        phase = LunarPhase(date)

        self.assertEqual(LunarPhases.FULL_MOON, phase.phase)

    def test_phase_should_be_first_quarter(self):
        pass

    def test_phase_should_be_last_quarter(self):
        pass

    def test_phase_should_be_waning_gibbous(self):
        pass

    def test_phase_should_be_waxing_crescent(self):
        pass

    def test_phase_should_be_waning_crescent(self):
        pass
