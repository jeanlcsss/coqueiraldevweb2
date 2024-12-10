# users/views/perfil_views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import PerfilForm
from ..models import Perfil

# Exibição do perfil do usuário logado
@login_required
def perfil(request):
    perfil = Perfil.objects.get(user=request.user)
    return render(request, 'users/perfil.html', {'perfil': perfil})

# Edição do perfil do usuário logado
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redireciona para a página de perfil após salvar
    else:
        form = PerfilForm(instance=request.user.perfil)
    return render(request, 'users/editar_perfil.html', {'form': form})
