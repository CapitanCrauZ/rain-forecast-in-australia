from django import views
from django.urls import path
from .views import home, show_form, log_out


urlpatterns = [
    path('', home),
    path('', show_form),
    path('accounts/', log_out, name='logout')
]