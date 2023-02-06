from rest_framework import status
from apps.users.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from apps.users.api.serializers import UserSerializer




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
    user = get_object_or_404(User)
    user_serializer = user_serializer(user, many = True)
    if pk is None:
        return user_serializer.Meta.model.objects.filter(state=True)
    return user_serializer.Meta.model.objects.filter(id = pk, state = True).first()



class HousingPagination(PageNumberPagination):
    page_size = 10

def pagination_list(request):
    query = User.objects.all()
    paginator = HousingPagination()
    result_page = paginator.paginate_queryset(query, request)
    serializer = UserSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)



def get(request, pk):
    user = get_object_or_404(User, pk = pk)
    if user is not None:
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status = status.HTTP_200_OK)
    return Response('user not found', status = status.HTTP_412_PRECONDITION_FAILED)

  

def create(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User Created'},status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


 
def update(request,pk=None):
    user = get_object_or_404(User, pk = pk, is_active= True)
    if user:
        user_serializer = UserSerializer(user, data = request.data, partial = True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status = status.HTTP_200_OK)
        return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)



def destroy(request,pk=None):
    user = get_object_or_404(User, pk = pk, is_active = True)
    if user:
        user.is_active = False
        user.save()
        return Response({'message': 'User Deleted'}, status = status.HTTP_200_OK)
    return Response({'error': 'User does not exist'}, status = status.HTTP_400_BAD_REQUEST)

    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def request_without_pk(request):
    
    if request.method == 'POST':
        return create(request)
    
    if request.method == 'GET':
        return pagination_list(request)

    return Response('Method not allowed', status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def request_with_pk(request, pk=None):

    if request.method == 'DELETE':
       return destroy(request,pk)

    if request.method == 'PUT':
        return update(request,pk)

    if request.method == 'GET':
        return get(request, pk)

    return Response('Method not allowed', status = status.HTTP_400_BAD_REQUEST)