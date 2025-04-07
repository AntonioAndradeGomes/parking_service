from django.shortcuts import render
from .models import Vehicle, VehicleType
from rest_framework import viewsets
from .serializers import VehiclesTypesSerializer, VehiclesSerializer

class VehiclesTypesViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehiclesTypesSerializer

class VehiclesViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehiclesSerializer
