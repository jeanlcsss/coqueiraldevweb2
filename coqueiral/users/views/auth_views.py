# users/views/auth_views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from ..forms import CustomUserCreationForm

# Login do usuário
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redireciona para a página inicial
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Logout do usuário
def user_logout(request):
    logout(request)
    return redirect('home')

# Registro de novo usuário
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redireciona após o registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
