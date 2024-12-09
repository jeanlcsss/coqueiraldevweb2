from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('pagina_principal/', views.pagina_principal, name='pagina_principal'),
    path('roupa/<int:roupa_id>/', views.detalhe_roupa, name='detalhe_roupa'),
    path('menu_usuario/', views.menu_usuario, name='menu_usuario'),
    path('menu_adm/', views.menu_adm, name='menu_adm'),
    path('adicionar_roupa/', views.adicionar_roupa, name='adicionar_roupa'),
    path('editar_roupa/<int:roupa_id>/', views.editar_roupa, name='editar_roupa'),
    path('remover_roupa/<int:roupa_id>/', views.remover_roupa, name='remover_roupa'),
]
