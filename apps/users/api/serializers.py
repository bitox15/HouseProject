from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password', 'email', 'name', 'last_name',]
        extra_kwargs = {'password': {'write_only': False}}

    def create(self, validated_data):
        user = User(
        email=validated_data['email'],
        username=validated_data['username'],
        name = validated_data['name'],
        last_name = validated_data['last_name'],
        password = validated_data['password'],
    )
        user.set_password(validated_data['password'])
        user.save()
        return user