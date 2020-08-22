from rest_framework import serializers
from ..models.citizen import Citizen
from ..models.home import Home


class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Home
        exclude = ['id']


class CitizenSerializer(serializers.ModelSerializer):

    home = HomeSerializer()

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


class WardSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()
    ward_no = serializers.IntegerField()
    # gender = CitizenSerializer()

    class Meta:
        model = Citizen
        fields = ['ward_no', 'gender', 'count']


class WardReligionSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()
    ward_no = serializers.IntegerField()

    class Meta:
        model = Citizen
        fields = ['ward_no', 'religion', 'count']


class LiteracySerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = Citizen
        fields = ['count', 'literacy']


class WardLiteracySerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = Citizen
        fields = ['count', 'ward_no', 'literacy']
