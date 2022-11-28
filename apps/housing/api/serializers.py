from rest_framework import serializers
from apps.housing.models import Housing, TypeHousing



class TypeHousingSerializer(serializers.ModelSerializer):
    model = TypeHousing
    fields = '__all__'






class HousingSerializer(serializers.ModelSerializer):
    
    class Meta:
       
        model = Housing
        fields = ['id', 'adress', 'department', 'phone_number', 'type', 'description','owner', 'price']
       
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'adress': instance.adress,
            
            'phone_number': instance.phone_number,
            'type': instance.type.type,
            'description': instance.description,
            'owner': instance.owner.username,
            'price': instance.price
        }
        
    #'department': instance.department.name,