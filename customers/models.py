from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    #os clientes no futuro vão usar isso num app
    user = models.OneToOneField( #ligação 1-1 para o usuário do Django
        User,
        on_delete=models.PROTECT, #se eu criar um cliente que está ligado a um user do Django, não vai deixar
        blank=True, 
        null=True, 
        related_name='customer',
        verbose_name='Cliente'
    )
    name = models.CharField(
        max_length=100, 
        verbose_name='Nome'
    )
    cpf = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        verbose_name='CPF'
    )
    phone = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        verbose_name='Telefone'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name='Atualizado em'
    )

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name