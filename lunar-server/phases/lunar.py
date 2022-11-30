from dataclasses import dataclass

from enum import Enum
from datetime import datetime, timezone
from skyfield.api import load
from skyfield.framelib import ecliptic_frame

from .utils import map_range

ORDERED_PHASES = [
    "New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
    "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"
]

RANGE_LEN = (1 / len(ORDERED_PHASES)) / 2


class LunarPhases(str, Enum):
    NEW_MOON = "New Moon"
    WAXING_CRESCENT = "Waxing Cresent"
    FIRST_QUARTER = "First Quarter"
    WAXING_GIBBOUS = "Waxing Gibbous"
    FULL_MOON = "Full Moon"
    WANING_GIBBOUS = "Waning Gibbous"
    LAST_QUARTER = "Last Quarter"
    WANING_CRESCENT = "Waning Crescent"


PHASE_RANGES = {
    LunarPhases.NEW_MOON: [1 - RANGE_LEN, RANGE_LEN * 1],
    LunarPhases.WAXING_CRESCENT: [RANGE_LEN * 1, RANGE_LEN * 3],
    LunarPhases.FIRST_QUARTER: [RANGE_LEN * 3, RANGE_LEN * 5],
    LunarPhases.WAXING_GIBBOUS: [RANGE_LEN * 5, RANGE_LEN * 7],
    LunarPhases.FULL_MOON: [RANGE_LEN * 7, RANGE_LEN * 9],
    LunarPhases.WANING_GIBBOUS: [RANGE_LEN * 9, RANGE_LEN * 11],
    LunarPhases.LAST_QUARTER: [RANGE_LEN * 11, RANGE_LEN * 13],
    LunarPhases.WANING_CRESCENT: [RANGE_LEN * 13, RANGE_LEN * 15]
}

# It's called the_range, since I don't want to clash with the range function


def in_range(val: float, the_range: [float, float]):
    start, end = the_range

    return val >= start and val < end \
        if start < end \
        else val > end or val <= start


# This is designated for the
PHASES_ASCII = """
@@ Phases of the Moon @@  11/96  (c)jgs

        _..._
      .:::::::.
     :::::::::::   NEW  MOON
     :::::::::::
     `:::::::::'
       `':::''
        _..._
      .::::. `.
     :::::::.  :    WAXING CRESCENT
     ::::::::  :
     `::::::' .'
       `'::'-'
        _..._
      .::::  `.
     ::::::    :    FIRST QUARTER
     ::::::    :
     `:::::   .'
       `'::.-'
        _..._
      .::'   `.
     :::       :    WAXING GIBBOUS
     :::       :
     `::.     .'
       `':..-'
        _..._
      .'     `.
     :         :    FULL MOON
     :         :
     `.       .'
       `-...-'
        _..._
      .'   `::.
     :       :::    WANING GIBBOUS
     :       :::
     `.     .::'
       `-..:''
        _..._
      .'  ::::.
     :    ::::::    LAST QUARTER
     :    ::::::
     `.   :::::'
       `-.::''
        _..._
      .' .::::.
     :  ::::::::    WANING CRESCENT
     :  ::::::::
     `. '::::::'
       `-.::''
        _..._
      .:::::::.
     :::::::::::    NEW MOON
     :::::::::::
     `:::::::::'
       `':::''
"""


@dataclass
class PhaseResult:
    illumination_pct: int
    phase_pct: int


class SkyFieldMoonProvider:

    def __init__(self):
        pass

    def phase(self, date=datetime.now()):
        """
        Taken from the example:
        https://rhodesmill.org/skyfield/examples.html#what-phase-is-the-moon-tonight
        """
        ts = load.timescale()
        t = ts.from_datetime(date)

        # Beware this actually downloads a database if
        # it does not exist in the root folder.
        eph = load('de421.bsp')
        sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

        e = earth.at(t)
        s = e.observe(sun).apparent()
        m = e.observe(moon).apparent()

        _, slon, _ = s.frame_latlon(ecliptic_frame)
        _, mlon, _ = m.frame_latlon(ecliptic_frame)
        phase = (mlon.degrees - slon.degrees) % 360.0

        percent = 100.0 * m.fraction_illuminated(sun)

        print(f"Phase (0°–360°): {phase:.1f}")
        print(f"Percent illuminated: {percent:.1f}%")

        return PhaseResult(percent, map_range(phase, 0, 360, 0, 1))


@dataclass
class LunarPhaseResult:
    illumination_pct: float
    phase_pct: float
    phase_name: str


class LunarPhase:
    """
    Each phase is split into its equal 8th part and then

    If a phase "moment" is inside the period, then the phase is equal to the

    This strategy is based on this article
    https://minkukel.com/en/various/calculating-moon-phase/
    """

    def __init__(self, date: datetime, moon_provider=SkyFieldMoonProvider()):
        self.date = date
        self._moon_provider = moon_provider
        self.phase = self._find_phase()

    def _find_phase(self):
        result = self._moon_provider.phase(self.date.astimezone(timezone.utc))

        phase = None

        print(f"{result.phase_pct} %")
        for phase_name, phase_range in PHASE_RANGES.items():
            print(f"{phase_name}: {phase_range}")
            if in_range(result.phase_pct, phase_range):
                phase = f"{phase_name}"
                break

        return LunarPhaseResult(result.illumination_pct,
                                result.phase_pct,
                                phase)
