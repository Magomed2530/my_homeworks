from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Advertisement, User
from .forms import AdvertisementForms


# def index(request):
#     return HttpResponse('Джанго-серсвер успешно запущен')

def index(request):
    advertisements = Advertisement.objects.all()  # advertisements - тип данных QwerySet (подобие списка)
    context = {'advertisements': advertisements}  # ключ словаря - имя, как обращаться к контексту в html файле
    return render(request, 'index.html', context=context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def adv_post(request):
    if request.method == 'POST':
        form = AdvertisementForms(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            #advertisement.user = request.user
            advertisement.user = User.objects.all()[0]
            advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    elif request.method == 'GET':
        form = AdvertisementForms()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context=context)

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')


