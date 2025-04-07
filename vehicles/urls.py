from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiclesTypesViewSet, VehiclesViewSet

router = DefaultRouter()

router.register('vehicles/types', VehiclesTypesViewSet, basename='veihicles-types')
router.register('vehicles', VehiclesViewSet, basename='veihicles')

urlpatterns = [
   path('', include(router.urls)),
]
