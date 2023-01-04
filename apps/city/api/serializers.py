from rest_framework import serializers
from apps.city.models import CityUbication


class CityUbicationSerializer(serializers.ModelSerializer):
    class Meta:

        model = CityUbication
        fields = '__all__'


        