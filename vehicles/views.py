from django.shortcuts import render
from .models import Vehicle, VehicleType
from rest_framework import viewsets
from .serializers import VehiclesTypesSerializer, VehiclesSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from core.permissions import IsOwnerOfVehicleOrRecord

class VehiclesTypesViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehiclesTypesSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]

class VehiclesViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehiclesSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user
        if(user.is_staff):
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)