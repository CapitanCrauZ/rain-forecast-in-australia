import email
from django.shortcuts import redirect, render
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from matplotlib.style import context
from numpy import save

# Create your views here.

def register(request):
    #GET
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            user_register = form.save()
            if user_register is not None:
                login(request, user_register)
                return redirect('log/profile.html')
    context = {
        'form':form
    }
    return render(request, 'log/register.html', context)
    #POST

def log(request):
    return render(request, 'log/index.html')

def log_out(request):
    logout(request)
    return redirect('/')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'log/profile.html')
    return redirect('home/')

    