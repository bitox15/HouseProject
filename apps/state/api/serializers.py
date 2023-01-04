from rest_framework import serializers
from apps.state.models import StateUbication


class StateUbicationSerializer(serializers.ModelSerializer):
    class Meta:

        model = StateUbication
        fields = '__all__'


        