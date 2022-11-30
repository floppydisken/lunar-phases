from rest_framework.serializers import Serializer, FloatField, CharField
from phases.lunar import LunarPhaseResult


class LunarPhaseResultSerializer(Serializer):
    illumination_pct = FloatField()
    phase_pct = FloatField()
    phase_name = CharField()
