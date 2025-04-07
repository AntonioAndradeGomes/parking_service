from rest_framework import serializers
from .models import Vehicle, VehicleType

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehiclesTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'