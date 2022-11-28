from rest_framework import serializers
from apps.city.models import CityUbication


class CityUbicationSerializer(serializers.ModelSerializer):
    class Meta:

        model = CityUbication
        fields = ['name','state']

    def to_representation(self, instance):
        return {
            'name': instance.name,
            'state': instance.state.name

        }
            
        