from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import ExtendedUserCreationForm


# login_view, profile_view, logout_view

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:  # если пользователь аутентифицирован
            return redirect(redirect_url)  # переход в профиль
        else:
            return render(request, 'app_auth/login.html')  # остаемся в логине
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # авторизация
        if user is not None:  # если пользователь с такими логином и паролем есть
            login(request, user)  # логинимся
            return redirect(redirect_url)  # переход в профиль
        # иначе остаемся в логине с выводом ошибки
        return render(request, 'app_auth/login.html', {"error": "Пользователь не найден"})

@login_required(login_url=reverse_lazy('login'))  # reverse_lazy - как reverse, но срабатывает только при обращении
def profile_view(request):
    return render(request, 'app_auth/profile.html')


def logout_view(request):
    logout(request)  # разлогинирование
    return redirect(reverse('login'))  # переход в логин


def register_view(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, user=user)
            return redirect(reverse('profile'))
    else:
        form = ExtendedUserCreationForm()
    context = {'form': form}
    return render(request, 'app_auth/register.html', context)
