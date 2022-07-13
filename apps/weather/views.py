from django.shortcuts import render

# Create your views here.

def weather (request):
    return render(request, 'weather/index.html')

def base (request): 
    return render(request, 'base/index.html')