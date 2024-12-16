from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField(default=False)  # Define se é um cliente
    is_staff = models.BooleanField(default=False)  # Define se é um adm

    def __str__(self):
        return self.username

class Perfil(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # Aponta para o modelo CustomUser
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    nome_completo = models.CharField(max_length=255)
    email = models.TextField(blank=False, null=False)
    data_de_nascimento = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.nome_completo
    
class Cliente(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='cliente')

    def __str__(self):
        return self.user.username

