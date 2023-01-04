from rest_framework import status
from apps.users.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny



from apps.users.api.serializers import UserSerializer


serializer_class = UserSerializer

def get_filter(filters):

    users = User.objects.filter(is_active = True)
    if 'name' in filters and filters['name'] != '':
        users = users.filter(name__icontains = filters['name'])
    if 'last_name' in filters and filters['last_name'] != '':
        users = users.filter(last_name__icontains = filters['last_name'])
    if 'username' in filters and filters['username'] != '':
        users = users.filter(username__icontains = filters['username'])
    if 'email' in filters and filters['email'] != '':
        users = users.filter(email__icontains = filters['email'])
    return users
    
    
def get_queryset(pk=None):
    if pk is None:
        return serializer_class.Meta.model.objects.filter(is_active=True)
    return serializer_class.Meta.model.objects.filter(id = pk, is_active = True).first()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list(request):
    users = get_filter(request.data)
    user_serializer = UserSerializer(users, many = True)
    return Response(user_serializer.data, status = status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request, pk):
    user = get_object_or_404(User, pk = pk)
    if user is not None:
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status = status.HTTP_200_OK)
    return Response('user not found', status = status.HTTP_412_PRECONDITION_FAILED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])   
def create(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User Created'},status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated]) 
def update(request,pk=None):
    user = get_object_or_404(User, pk = pk, is_active= True)
    if user:
        user_serializer = UserSerializer(user, data = request.data, partial = True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status = status.HTTP_200_OK)
        return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  
def destroy(request,pk=None):
    user = get_object_or_404(User, pk = pk, is_active = True)
    if user:
        user.is_active = False
        user.save()
        return Response({'message': 'User Deleted'}, status = status.HTTP_200_OK)
    return Response({'error': 'User does not exist'}, status = status.HTTP_400_BAD_REQUEST)

    

    