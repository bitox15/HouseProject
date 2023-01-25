from django.shortcuts import render
from apps.state.models import StateUbication
from apps.state.api.serializers import StateUbicationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


def get_queryset(pk=None):
    state_serializer = StateUbicationSerializer
    if pk is None:
        return state_serializer.Meta.model.objects.filter(is_active=True)
    return state_serializer.Meta.model.objects.filter(id = pk, is_active = True).first()


def get_filter(filters):
    state = StateUbication.objects.filter(is_active = True)
    if 'name' in filters and filters['name'] != '':
        state = state.filter(name__icontains = filters['name'])
    return state



def get(request, pk):
    state = get_object_or_404(StateUbication, pk = pk)
    if state is not None:
        state_serializer = StateUbicationSerializer(state)
        return Response(state_serializer.data, status = status.HTTP_200_OK)



def list(request):
    states = get_filter(request.data)
    state_serializer = StateUbicationSerializer(states, many = True)
    return Response(state_serializer.data, status = status.HTTP_200_OK)



def create(request):
    state_serializer = StateUbicationSerializer(data = request.data)
    if state_serializer.is_valid():
        state_serializer.save()
        return Response({'message': 'State Created'},status = status.HTTP_201_CREATED)
    return Response(state_serializer.errors, status = status.HTTP_400_BAD_REQUEST)



def update(request,pk=None):
    state = get_object_or_404(StateUbication, pk = pk, is_active= True)
    if state:
        state_serializer = StateUbicationSerializer(state, data = request.data, partial = True)
        if state_serializer.is_valid():
            state_serializer.save()
            return Response(state_serializer.data,status = status.HTTP_200_OK)
        return Response(state_serializer.errors,status = status.HTTP_400_BAD_REQUEST)


  
def destroy(request,pk=None):
    state = get_object_or_404(StateUbication, pk = pk, is_active = True)
    if state:
        state.is_active = False
        state.save()
        return Response({'message': 'State Deleted'}, status = status.HTTP_200_OK)
    return Response({'error': 'State does not exist'}, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def request_without_pk(request):
    
    if request.method == 'POST':
        return create(request)
    
    if request.method == 'GET':
        return list(request)

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