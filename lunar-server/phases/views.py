from datetime import datetime

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

import ephem

phases = [
    "New Moon",
    "Waxing Crescent",
    "First Quarter",
    "Waxing Gibbous",
    "Full Moon",
    "Waning Gibbous",
    "Last Quarter",
    "Waning Crescent"
]


class LunarPhase:
    def __init__(self, ):
        pass

    def __lt__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __gt__(self, other):
        pass


@api_view(["GET"])
def handle_get(request: Request, date: datetime):
    prev_new_moon = ephem.prev_new_moon(date)
    next_new_moon = ephem.next_new_moon(date)
    prev_first_quarter = ephem.prev_first_quarter_moon(date)
    next_first_quarter = ephem.next_first_quarter_moon(date)
    prev_last_quarter = ephem.prev_last_quarter_moon(date)
    next_last_quarter = ephem.next_last_quarter_moon(date)
    prev_full_moon = ephem.prev_full_moon(date)
    next_full_moon = ephem.next_full_moon(date)

    return Response("new moon")
