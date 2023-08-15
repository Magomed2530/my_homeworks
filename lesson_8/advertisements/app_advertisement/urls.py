from django.urls import path, include
from .views import index, top_sellers, advertisement_post, login, profile, register

urlpatterns = [
    path('', index, name='main_page'),  # пустой путь - это заглавная страница
    path('top-sellers/', top_sellers, name='top_sel'),
    path('advertisement-post/', advertisement_post, name='advert_post'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register')
]
