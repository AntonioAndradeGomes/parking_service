from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customers.views import CustomerViewSet

router = DefaultRouter()

router.register('customers', CustomerViewSet, basename='customers')

urlpatterns = [
    path('', include(router.urls)),
]
