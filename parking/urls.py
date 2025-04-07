from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkingSpotViewSet, ParkingRecordViewSet

router = DefaultRouter()

router.register('parking/spots', ParkingSpotViewSet, basename='parking_spots')

router.register('parking/records', ParkingRecordViewSet, basename='parking_records')

urlpatterns = [
   path('', include(router.urls)),
]
