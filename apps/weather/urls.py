from django import views
from .views import weather, base
from django.urls import path

urlpatterns = [
    path('', weather, name='weather'),
    path('', base, name='base'),
]