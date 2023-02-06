from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from apps.housing.api.serializers import HousingSerializer
from apps.housing.models import Housing
from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView


def get_filter(filters):

    housing = Housing.objects.filter()
    if 'address' in filters and filters['address'] != '':
        housing = housing.filter(address__icontains = filters['address'])
    if 'phone_number' in filters and filters['phone_number'] != '':
        housing = housing.filter(phone_number__icontains = filters['phone_number'])
    if 'price' in filters and filters['price'] != '':
        housing = housing.filter(price__icontains = filters['price'])
    return housing



def get(request, pk):
    housing = get_object_or_404(Housing, pk = pk)
    if housing is not None:
        housing_serializer = HousingSerializer(housing)
        return Response(housing_serializer.data, status = status.HTTP_200_OK)
    


def get_queryset(pk=None):
    housing = get_object_or_404(Housing)
    housing_serializer = HousingSerializer(housing, many = True)
    if pk is None:
        return housing_serializer.Meta.model.objects.filter(state=True)
    return housing_serializer.Meta.model.objects.filter(id = pk, state = True).first()



class HousingPagination(PageNumberPagination):
    page_size = 10

def pagination_list(request):
    query = Housing.objects.all()
    paginator = HousingPagination()
    result_page = paginator.paginate_queryset(query, request)
    serializer = HousingSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
 

    
def create(request):
    serializer = HousingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Housing Created'},status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


  
def update(request,pk=None):
    housing = get_object_or_404(Housing, pk = pk, is_active = True)
    if housing:
        housing_serializer = HousingSerializer(housing, data = request.data, partial = True)
        if housing_serializer.is_valid():
            housing_serializer.save()
            return Response(housing_serializer.data,status = status.HTTP_200_OK)
        return Response(housing_serializer.errors,status = status.HTTP_400_BAD_REQUEST)



def destroy(request,pk=None):
    housing = get_object_or_404(Housing, pk = pk, is_active = True)
    if housing:
        housing.is_active = False
        housing.save()
        return Response({'message': 'Housing Deleted'}, status = status.HTTP_200_OK)
    return Response({'error': 'Housing does not exist'}, status = status.HTTP_400_BAD_REQUEST)




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







