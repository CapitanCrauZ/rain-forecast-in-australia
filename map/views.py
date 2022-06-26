from django.shortcuts import render, redirect, reverse
from django.conf import settings


def map(request):
    return render(request, 'map/map.html')
