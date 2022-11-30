from datetime import datetime

from dataclasses import asdict

from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .lunar import LunarPhase
from .serializers import LunarPhaseResultSerializer


class LunarView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, format=None):
        date = datetime.now()
        lunar_phase = LunarPhase(date)
        serializer = LunarPhaseResultSerializer(lunar_phase.phase)

        return Response(serializer.data)
