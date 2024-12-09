from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from .models import Roupa
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'coqueiral/index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('pagina_principal')
    else:
        form = AuthenticationForm()
    return render(request, 'coqueiral/login.html', {'form': form})

def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pagina_principal')
    else:
        form = UserCreationForm()
    return render(request, 'coqueiral/cadastro.html', {'form': form})

def pagina_principal(request):
    roupas = Roupa.objects.all()
    return render(request, 'coqueiral/pagina_principal.html', {'roupas': roupas})

def detalhe_roupa(request, roupa_id):
    roupa = Roupa.objects.get(id=roupa_id)
    return render(request, 'coqueiral/detalhe_roupa.html', {'roupa': roupa})

@login_required
def menu_usuario(request):
    if request.user.is_admin:
        return redirect('menu_adm')  # Caso seja administrador
    return render(request, 'coqueiral/menu_usuario.html', {'user': request.user})

@login_required
def menu_adm(request):
    if not request.user.is_admin:
        return redirect('pagina_principal')  # Bloqueia usuários comuns
    roupas = Roupa.objects.all()
    return render(request, 'coqueiral/menu_adm.html', {'roupas': roupas})

# Adicionar roupa
@login_required
def adicionar_roupa(request):
    if not request.user.is_admin:
        return redirect('pagina_principal')
    if request.method == 'POST':
        form = RoupaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu_adm')
    else:
        form = RoupaForm()
    return render(request, 'coqueiral/adicionar_roupa.html', {'form': form})

# Editar roupa
@login_required
def editar_roupa(request, roupa_id):
    if not request.user.is_admin:
        return redirect('pagina_principal')
    roupa = get_object_or_404(Roupa, id=roupa_id)
    if request.method == 'POST':
        form = RoupaForm(request.POST, request.FILES, instance=roupa)
        if form.is_valid():
            form.save()
            return redirect('menu_adm')
    else:
        form = RoupaForm(instance=roupa)
    return render(request, 'coqueiral/editar_roupa.html', {'form': form, 'roupa': roupa})

# Remover roupa
@login_required
def remover_roupa(request, roupa_id):
    if not request.user.is_admin:
        return redirect('pagina_principal')
    roupa = get_object_or_404(Roupa, id=roupa_id)
    roupa.delete()
    return redirect('menu_adm')