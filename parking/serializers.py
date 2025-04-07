from .models import ParkingSpot, ParkingRecord
from rest_framework import serializers

class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = '__all__'

class ParkingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingRecord
        fields = '__all__'