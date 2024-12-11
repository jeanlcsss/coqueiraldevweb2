from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('criar/', views.criar_produto, name='criar_produto'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('excluir/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
]