from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('profile'))
        return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('profile'))
    return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден'})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def register(request): 
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password1') 
            user = authenticate(request, username=username, password=password) 
            login(request, user) 
            return redirect(reverse('profile'))
    else: 
        form = CustomUserCreationForm() 
    return render(request, 'app_auth/register.html', {'form': form})