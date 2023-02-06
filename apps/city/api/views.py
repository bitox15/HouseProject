from django.shortcuts import render
from apps.city.models import CityUbication
from apps.city.api.serializers import CityUbicationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


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



def get(request, pk):
    city = get_object_or_404(CityUbication, pk = pk)
    if city is not None:
        city_serializer = CityUbicationSerializer(city)
        return Response(city_serializer.data, status = status.HTTP_200_OK)



class HousingPagination(PageNumberPagination):
    page_size = 10

def pagination_list(request):
    query = CityUbication.objects.all()
    paginator = HousingPagination()
    result_page = paginator.paginate_queryset(query, request)
    serializer = CityUbicationSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


 
def create(request):
    city_serializer = CityUbicationSerializer(data = request.data)
    if city_serializer.is_valid():
        city_serializer.save()
        return Response({'message': 'city Created'},status = status.HTTP_201_CREATED)
    return Response(city_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    
def update(request,pk=None):
    city = get_object_or_404(CityUbication, pk = pk, is_active= True)
    if city:
        city_serializer = CityUbicationSerializer(city, data = request.data, partial = True)
        if city_serializer.is_valid():
            city_serializer.save()
            return Response(city_serializer.data,status = status.HTTP_200_OK)
        return Response(city_serializer.errors,status = status.HTTP_400_BAD_REQUEST)



def destroy(request,pk=None):
    city = get_object_or_404(CityUbication, pk = pk, is_active = True)
    if city:
        city.is_active = False
        city.save()
        return Response({'message': 'City Deleted'}, status = status.HTTP_200_OK)
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