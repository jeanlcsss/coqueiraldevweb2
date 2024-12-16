# users/urls.py
from django.urls import path
from .views import auth_views, perfil_views, cliente_views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.user_login, name='login'),
    path('logout/', auth_views.user_logout, name='logout'),
    path('register/', auth_views.register, name='register'),
    
    path('perfil/', perfil_views.perfil, name='perfil'),
    path('editar-perfil/', perfil_views.editar_perfil, name='editar_perfil'),
    
    path('cliente/', cliente_views.acesso_cliente, name='acesso_cliente'),
]
