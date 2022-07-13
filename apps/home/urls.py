from django import views
from django.urls import path
from .views import exit, profile, home, base, log


urlpatterns = [
    path('', home, name='home'),
    path('', base, name='base'),
    path('log/', log, name='log'),
    path('accounts/', exit, name='exit'),
    path('profile/', profile, name='profile'),
]