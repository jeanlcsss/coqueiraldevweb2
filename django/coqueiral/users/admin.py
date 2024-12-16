from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Perfil, Cliente

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_customer')

admin.site.register(Perfil)
admin.site.register(Cliente)

