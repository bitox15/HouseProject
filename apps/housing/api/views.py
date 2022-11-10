from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.housing.api.serializers import HousingSerializer

class HousingViewSet(viewsets.ModelViewSet):
    serializer_class = HousingSerializer
    
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()

    
    def list(self,request):
        housing_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(housing_serializer.data, status = status.HTTP_200_OK)

    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Housing Created'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            housing_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if housing_serializer.is_valid():
                housing_serializer.save()
                return Response(housing_serializer.data,status = status.HTTP_200_OK)
            return Response(housing_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    
    def destroy(self,request,pk=None):
        housing = self.get_queryset().filter(id=pk).first()
        if housing:
            housing.state = False
            housing.save()
            return Response({'message': 'Housing Deleted'}, status = status.HTTP_200_OK)
        return Response({'error': 'Housing does not exist'}, status = status.HTTP_400_BAD_REQUEST)

    
