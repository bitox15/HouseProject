from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.users.models import User
from apps.users.api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.filter()