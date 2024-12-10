# users/forms.py
from django import forms
from .models import CustomUser, Perfil

# Formulário para criar novo usuário (CustomUser)
class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'is_customer', 'is_staff', 'password']
    password = forms.CharField(widget=forms.PasswordInput)

# Formulário para editar perfil do usuário
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome_completo', 'email', 'data_de_nascimento']
