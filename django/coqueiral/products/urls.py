from django.urls import path
from .views import criar_produto, listar_produtos, detalhes_produto, editar_produto, excluir_produto

app_name = 'products'

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('<int:produto_id>/', detalhes_produto, name='detalhes_produto'),
    path('criar/', criar_produto, name='criar_produto'),
    path('editar/<int:produto_id>/', editar_produto, name='editar_produto'),
    path('excluir/<int:produto_id>/', excluir_produto, name='excluir_produto'),
]