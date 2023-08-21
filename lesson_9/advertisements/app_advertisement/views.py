from django.http import HttpResponse
from django.shortcuts import render
from .models import Advertisement


# def index(request):
#     return HttpResponse('Джанго-серсвер успешно запущен')

def index(request):
    advertisements = Advertisement.objects.all()  # advertisements - тип данных QwerySet (подобие списка)
    context = {'advertisements': advertisements}  # ключ словаря - имя, как обращаться к контексту в html файле
    return render(request, 'index.html', context=context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')


