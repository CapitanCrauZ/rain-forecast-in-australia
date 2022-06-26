from django import views
from django.urls import path
from .views import map

urlpatterns = [
    path('', map, name='map')
]