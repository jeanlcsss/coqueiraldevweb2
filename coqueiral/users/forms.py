# users/forms.py
from django import forms
from .models import CustomUser, Perfil
from django.contrib.auth.forms import UserCreationForm

# Formulário para criar novo usuário (CustomUser)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
    password = forms.CharField(widget=forms.PasswordInput)

# Formulário para editar perfil do usuário
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome_completo', 'email', 'data_de_nascimento']
