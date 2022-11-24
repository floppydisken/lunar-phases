from datetime import datetime

import ephem

ORDERED_PHASES = [
    "New Moon",
    "Waxing Crescent",
    "First Quarter",
    "Waxing Gibbous",
    "Full Moon",
    "Waning Gibbous",
    "Last Quarter",
    "Waning Crescent"
]

RANGE_LEN = (1 / len(ORDERED_PHASES)) / 2

PHASE_RANGES = {
    "new_moon":        [1 - RANGE_LEN,  RANGE_LEN * 1],  # This spills over
    "waxing_cresent":  [RANGE_LEN * 1,  RANGE_LEN * 3],
    "first_quarter":   [RANGE_LEN * 3,  RANGE_LEN * 5],
    "waxing_gibbous":  [RANGE_LEN * 5,  RANGE_LEN * 7],
    "full_moon":       [RANGE_LEN * 7,  RANGE_LEN * 9],
    "waning_gibbous":  [RANGE_LEN * 9,  RANGE_LEN * 11],
    "last_quarter":    [RANGE_LEN * 11, RANGE_LEN * 13],
    "waning_crescent": [RANGE_LEN * 13, RANGE_LEN * 15]
}


# It's called the_range, since I don't want to clash with the range function
def in_range(val: float, the_range: [float, float]):
    start, end = the_range
    return val > start and val < end


class LunarPhase:
    """
    Each phase is split into its equal 8th part and then

    If a phase "moment" is inside the period, then the phase is equal to the

    This strategy is based on this article https://minkukel.com/en/various/calculating-moon-phase/
    """

    def __init__(self, date: datetime):
        self.date = date

        self._moon = ephem.Moon()
        self._moon.compute(date)

        self.phase = self._find_phase()

    def _find_phase(self):
        phase_pct = self._moon.phase

        phase = None

        for phase_name, phase_range in PHASE_RANGES.items():
            if in_range(phase_pct, phase_range):
                phase = phase_name
                break

        return phase

    def __lt__(self, other):
        return self.phase == other.phase

    def __eq__(self, other):
        return self.phase == other.phase

    def __gt__(self, other):
        pass
