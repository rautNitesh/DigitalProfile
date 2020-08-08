from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView

from ..models.citizen import Citizen
from ..serializers.citizen_serializer import CitizenSerializer


class CitizenViewSet(ListAPIView):

    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
