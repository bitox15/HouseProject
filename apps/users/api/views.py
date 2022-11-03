from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.users.models import User
from apps.users.api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active=True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, is_active = True).first()

    
    def list(self,request):
        user_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(user_serializer.data, status = status.HTTP_200_OK)

    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User Created'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            user_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status = status.HTTP_200_OK)
            return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    
    def destroy(self,request,pk=None):
        user = self.get_queryset().filter(id=pk).first()
        if user:
            user.is_active = False
            user.save()
            return Response({'message': 'User Deleted'}, status = status.HTTP_200_OK)
        return Response({'error': 'User does not exist'}, status = status.HTTP_400_BAD_REQUEST)

    

    