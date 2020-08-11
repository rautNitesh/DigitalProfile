from django.db.models import Count
from django.http import JsonResponse

from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status

from ..models.citizen import Citizen
from ..serializers.citizen_serializer import CitizenSerializer, ReligionSerializer, GenderSerializer


class CitizenView(ListAPIView):

    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer


class GenderCount(APIView):

    def get_queryset(self):
        queryset = Citizen.objects.values(
            'gender').annotate(count=Count('gender'))
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = GenderSerializer(queryset, many=True)
        return Response(serializer.data)


class ReligionCountView(APIView):

    def get_queryset(self):
        queryset = Citizen.objects.annotate(count=Count('religion'))
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ReligionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
