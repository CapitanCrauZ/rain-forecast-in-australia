from django import views
from django.urls import path
from .views import register, log, log_out, profile


urlpatterns = [
    path('', log, name='login'),
    path('register/', register, name='register'),
    path('logout/', log_out, name='logout'),
    path('profile/', profile, name='profile')

]