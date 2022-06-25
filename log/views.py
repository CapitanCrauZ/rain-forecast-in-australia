from django.shortcuts import render

# Create your views here.

def log(request):
    return render(request, 'log/index.html')