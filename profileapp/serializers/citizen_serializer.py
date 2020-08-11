from rest_framework import serializers
from ..models.citizen import Citizen


class CitizenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Citizen
        exclude = ['id']


class GenderSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = Citizen
        fields = ['gender', 'count']


class ReligionSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = Citizen
        fields = ['religion', 'count']
