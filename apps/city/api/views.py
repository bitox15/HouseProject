from django.shortcuts import render
from apps.city.models import CityUbication
from apps.city.api.serializers import CityUbicationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404



def get_queryset(pk=None):
    city_serializer = CityUbicationSerializer
    if pk is None:
        return city_serializer.Meta.model.objects.filter(is_active=True)
    return city_serializer.Meta.model.objects.filter(id = pk, is_active = True).first()


def get_filter(filters):
    city = CityUbication.objects.filter(is_active = True)
    if 'name' in filters and filters['name'] != '':
        city = city.filter(name__icontains = filters['name'])
    return city


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request, pk):
    city = get_object_or_404(CityUbication, pk = pk)
    if city is not None:
        city_serializer = CityUbicationSerializer(city)
        return Response(city_serializer.data, status = status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list(request):
    cities = get_filter(request.data)
    city_serializer = CityUbicationSerializer(cities, many = True)
    return Response(city_serializer.data, status = status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])   
def create(request):
    city_serializer = CityUbicationSerializer(data = request.data)
    if city_serializer.is_valid():
        city_serializer.save()
        return Response({'message': 'city Created'},status = status.HTTP_201_CREATED)
    return Response(city_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])    
def update(request,pk=None):
    city = get_object_or_404(CityUbication, pk = pk, is_active= True)
    if city:
        city_serializer = CityUbicationSerializer(city, data = request.data, partial = True)
        if city_serializer.is_valid():
            city_serializer.save()
            return Response(city_serializer.data,status = status.HTTP_200_OK)
        return Response(city_serializer.errors,status = status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])   
def destroy(request,pk=None):
    city = get_object_or_404(CityUbication, pk = pk, is_active = True)
    if city:
        city.is_active = False
        city.save()
        return Response({'message': 'City Deleted'}, status = status.HTTP_200_OK)
    return Response({'error': 'User does not exist'}, status = status.HTTP_400_BAD_REQUEST)