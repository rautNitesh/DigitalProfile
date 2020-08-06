from rest_framework import serializers
from ..models.citizen import Citizen


class CitizenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Citizen
        exclude = ['id']
