# users/views/cliente_views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Exibição da página de cliente (somente para usuários do tipo 'cliente')
@login_required
def acesso_cliente(request):
    if not request.user.is_customer:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    return render(request, 'users/cliente.html')
