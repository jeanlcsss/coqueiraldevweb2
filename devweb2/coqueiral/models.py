from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Evita conflitos com o modelo padrão do Django
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Evita conflitos com o modelo padrão do Django
        blank=True,
    )

class Roupa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='roupas/')
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compras')
    roupa = models.ForeignKey(Roupa, on_delete=models.CASCADE)
    data_compra = models.DateTimeField(auto_now_add=True)
    quantidade = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calcular o total automaticamente
        self.total = self.quantidade * self.roupa.preco
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario.username} - {self.roupa.nome} em {self.data_compra}"

class LogAdmin(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_admin': True})
    acao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ação: {self.acao} por {self.admin.username} em {self.data}"
