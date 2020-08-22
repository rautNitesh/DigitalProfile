from django.db.models import Count, Q, Sum
from django.http import JsonResponse

from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status

from ..models.citizen import Citizen
from ..models.home import Home
from ..serializers.citizen_serializer import (CitizenSerializer,
                                              ReligionSerializer, GenderSerializer, WardSerializer,
                                              WardReligionSerializer, LiteracySerializer,
                                              WardLiteracySerializer)


class CitizenView(ListAPIView):
    """Lists all the citizens in model Citizen """
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer


class CitizenSearchView(ListAPIView):

    """Search based on names """
    serializer_class = CitizenSerializer

    def get_queryset(self):
        name = self.kwargs['slug']
        queryset = Citizen.objects.filter(name=name)
        return queryset


class GenderCount(APIView):
    """Total no of different gender citizen in whole LG"""

    def get_queryset(self):
        queryset = Citizen.objects.values(
            'gender').annotate(count=Count('gender'))
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = GenderSerializer(queryset, many=True)
        return Response(serializer.data)


class ReligionCountView(APIView):
    """Total no of different religion citizen in whole LG"""

    def get_queryset(self):
        queryset = Citizen.objects.annotate(count=Count('religion'))
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ReligionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WardGenderCount(APIView):
    data = []
    """Total no of people in different ward based on gender """

    def get_queryset(self):
        queryset = Citizen.objects.values('ward_no', 'gender').annotate(
            count=Count('gender'))
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = WardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WardReligionCount(APIView):
    """Counts no of different religion people in different ward """

    def get_queryset(self):
        queryset = Citizen.objects.values('ward_no', 'religion').annotate(
            count=Count('religion'))
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = WardReligionSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class LiteracyCount(APIView):

    def get_queryset(self):
        queryset = Citizen.objects.values(
            'literacy').annotate(count=Count('literacy'))
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = LiteracySerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class WardLiteracyCount(APIView):

    def get_queryset(self):
        queryset = Citizen.objects.values(
            'ward_no', 'literacy').annotate(count=Count('literacy'))
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = WardLiteracySerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
