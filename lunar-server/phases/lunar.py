from datetime import datetime

import ephem


class PhaseRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class LunarPhase:
    """
    The phases of the moon. Represented by looking in a timeperiod +-1 day
    from the given datetime.

    If a phase "moment" is inside the period, then the phase is equal to the

    This strategy is based on this article https://minkukel.com/en/various/calculating-moon-phase/
    """

    _ordered_phases = [
        "New Moon",
        "Waxing Crescent",
        "First Quarter",
        "Waxing Gibbous",
        "Full Moon",
        "Waning Gibbous",
        "Last Quarter",
        "Waning Crescent"
    ]

    def __init__(self, date: datetime):
        self.phase = self._find_phase(date)

    def _find_phase(self, date: datetime):
        print(date)

        # TODO: Simple graph to demonstrate the phases and range_len
        range_len = (1 / len(self._ordered_phases)) / 2

        phases = {
            "new_moon": [1 - range_len, range_len * 1],  # This spills over
            "waxing_cresent": [range_len * 1, range_len * 3],
            "first_quarter": [range_len * 3, range_len * 5],
            "waxing_gibbous": [range_len * 5, range_len * 7],
            "full_moon": [range_len * 7, range_len * 9],
            "waning_gibbous": [range_len * 9, range_len * 11],
            "last_quarter": [range_len * 11, range_len * 13],
            "waning_crescent": [range_len * 13, range_len * 15]
        }

        moon = ephem.Moon()
        moon.compute(date)

        phase_pct = moon.phase

        phase = None

        for phase_name, phase_range in phases.items():
            start, end = phase_range

            if phase_pct > start and phase_pct < end:
                phase = phase_name
                break

        print("Phases", phases)
        print(f"Found phase {phase}")

        return phase

    def __lt__(self, other):
        return self.phase == other.phase

    def __eq__(self, other):
        return self.phase == other.phase

    def __gt__(self, other):
        pass
