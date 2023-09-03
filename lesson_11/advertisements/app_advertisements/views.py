from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .models import Advertisement
from .forms import AdvertisementForm


# def index(request):
#     return HttpResponse('Успешно!')

def index(request):
    title = request.GET.get('query')
    print(title)
    if title:
        advertisements = Advertisement.objects.filter(title__icontains=title)
        # title=title / title__contains=title / title__icontains=title
        # price__lt / price__gt / price__lte / price__gte
    else:
        advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements, 'title': title}
    return render(request, 'app_advertisements/index.html', context=context)

User = get_user_model()

def top_sellers(request):
    users = User.objects.annotate(
        adv_count=Count('advertisement')
    ).order_by('-adv_count') # новая колонка adv_count
    context = {'users': users}
    return render(request, 'app_advertisements/top-sellers.html', context=context)

def adv_detail(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {'advertisement': advertisement}
    return render(request, 'app_advertisements/advertisement.html', context=context)

# если авторизован -> функция доступна, если нет -> переход в логин
@login_required(login_url=reverse_lazy('login'))  # reverse_lazy - как reverse, но срабатывает только при обращении
def adv_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main_page')
            return redirect(url)

    elif request.method == "GET":
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context=context)

