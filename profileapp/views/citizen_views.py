from rest_framework import viewsets

from ..models.citizen import Citizen
from ..serializers.user_serializer import CitizenSerializer


class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
