from django.conf import Settings
from django.shortcuts import redirect, render
from joblib import load
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required
def home(request):
    return render(request, 'home/index.html')

def show_form(request):
   if request.method == 'GET':
     return render(request, "home/index.html")
   elif request.method == 'POST':
     mejor_modelo = load(Settings.RUTA_MODELO)
     Location = print(request.POST["Location"])
     MinTemp = print(request.POST["MinTemp"])
     Evaporation = print(request.POST["Evaporation"])
     WindGustSpeed = print(request.POST["WindGustSpeed"])
     AvgWindSpeed = print(request.POST["AvgWindSpeed"])
     AvgHumidity = print(request.POST["AvgHumidity"])
     AvgPressure = print(request.POST["AvgPressure"])
     AvgCloud = print(request.POST["AvgCloud"])
     salida = {
         "predict": int(mejor_modelo.predict(([Location, MinTemp, Evaporation, WindGustSpeed, AvgWindSpeed, AvgHumidity, AvgPressure, AvgCloud]))[0])
     }
     print(salida)
     return render(request, "home/index.html", context = salida)

def log_out(request):
  logout(request)
  return redirect('/')

def profile(request):
  return render(request, 'log/profile.html')