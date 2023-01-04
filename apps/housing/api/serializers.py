from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from apps.housing.models import Housing, TypeHousing
from apps.city.models import CityUbication
from apps.state.models import StateUbication




class TypeHousingSerializer(serializers.ModelSerializer):
    model = TypeHousing
    fields = ['__all__']





class HousingSerializer(serializers.ModelSerializer):
    
    class Meta:
       
        model = Housing
        fields = ['id', 'address', 'department', 'phone_number', 'type', 'description','owner', 'price']
        
    

    def to_representation(self,instance):
       
        data = {
                'id': instance.id,
                'address': instance.address,
                
                'phone_number': instance.phone_number,
                'type': instance.type.type,
                'description': instance.description,
                'owner': instance.owner.username if instance.owner is not None else '',
                'department': instance.department.name if instance.department is not None else '',
                'price': instance.price
            }
        return data
        
    #'department': instance.department.name,