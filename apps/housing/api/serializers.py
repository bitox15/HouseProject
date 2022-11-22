from rest_framework import serializers
from apps.housing.models import Housing



class HousingSerializer(serializers.ModelSerializer):
    
    
    class Meta:
       
        model = Housing
        fields = ['id', 'adress', 'department', 'phone_number', 'type', 'description','owner', 'price']
       
