from django.urls import path, include
from .views import index, top_sellers, adv_post, login, profile, register

urlpatterns = [
    path('', index, name='main_page'),  # пустой путь - это заглавная страница
    path('top-sellers/', top_sellers, name='top-sel'),
    path('advertisement_post/', adv_post, name='adv-post'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register')
]
