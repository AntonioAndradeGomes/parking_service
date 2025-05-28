from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    ##só os usuários com permissão de administrador podem acessar este endpoint 
    #quem consegue ver os clientes, ter acesso aos clientes: somente administradores, também precisa passar pela permissão de modelo do Django
    permission_classes = [DjangoModelPermissions, IsAdminUser]