from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password', 'email', 'name', 'last_name', 'is_superuser']
        extra_kwargs = {'password': {'write_only': False}}

    def create(self, validated_data):
        user = User(
        username=validated_data['username'],    
        email=validated_data['email'],
        name = validated_data['name'],
        last_name = validated_data['last_name'],
        password = validated_data['password'],
        is_superuser = validated_data['is_superuser']
        
    )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self,instance,validated_data):
        update_user = super().update(instance,validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user