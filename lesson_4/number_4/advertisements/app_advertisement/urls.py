from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index)  # пустой путь - это заглавная страница
]
