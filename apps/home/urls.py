from django import views
from django.urls import path
from .views import home, log_out, profile, show_form


urlpatterns = [
    # path('', home),
    path('', show_form),
    path('accounts/', log_out, name='logout'),
    path('profile/', profile, name='profile'),
]