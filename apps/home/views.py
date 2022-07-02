from django.conf import Settings
from django.shortcuts import redirect, render, HttpResponse
from joblib import load
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from joblib import dump
import warnings
import sys


warnings.filterwarnings('ignore')

# Create your views here.

# MinTemp 1.5 - 

@login_required
def home(request):
    return render(request, 'home/index.html')

@login_required
def show_form(request):
    print(sys.argv[1:])
    mejor_modelo = load(".\model\mejor_modelo.joblib")
    if request.method == 'GET':
      # print(mejor_modelo.predict([[19.5, 6.2, 42.6, 18.5, 88.0, 1017.50, 8.0, 1.0]]))
      return render(request, "home/index.html")
    elif request.method == 'POST':
      # mejor_modelo = load(Settings.RUTA_MODELO)
      MinTemp = (request.POST['MinTemp'])
      Evaporation = (request.POST['Evaporation'])
      WindGustSpeed = (request.POST['WindGustSpeed'])
      AvgWindSpeed = (request.POST['AvgWindSpeed'])
      AvgHumidity = (request.POST['AvgHumidity'])
      AvgPressure = (request.POST['AvgPressure'])
      AvgCloud = (request.POST['AvgCloud'])
      RainToday = (request.POST['RainToday'])
      salida = {
          "predict": int(mejor_modelo.predict(([[MinTemp, Evaporation, WindGustSpeed, AvgWindSpeed, AvgHumidity, AvgPressure, AvgCloud, RainToday]]))[0])
      }
      print(salida)
      return render(request, "home/index.html", context = salida)
    salida = salida.cleaned_data()
    salida = salida.save()

    
      

def log_out(request):
  logout(request)
  return redirect('/')

def profile(request):
  return render(request, 'log/profile.html')