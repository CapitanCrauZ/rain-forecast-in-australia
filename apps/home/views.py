from django.shortcuts import redirect, render
from joblib import load
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import warnings
import sys


warnings.filterwarnings('ignore')

# Create your views here.

def base(request):
  return render(request, 'base/index.html')

@login_required
def home(request):
    print(sys.argv[1:])
    predict_model = load(".\model\predict-model.joblib")
    if request.method == 'GET':
      return render(request, "home/index.html")
    elif request.method == 'POST':
      MinTemp = (request.POST['MinTemp'])
      Evaporation = (request.POST['Evaporation'])
      WindGustSpeed = (request.POST['WindGustSpeed'])
      AvgWindSpeed = (request.POST['AvgWindSpeed'])
      AvgHumidity = (request.POST['AvgHumidity'])
      AvgPressure = (request.POST['AvgPressure'])
      AvgCloud = (request.POST['AvgCloud'])
      RainToday = (request.POST['RainToday'])
      salida = {
          "predict": int(predict_model.predict(([[MinTemp, Evaporation, WindGustSpeed, AvgWindSpeed, AvgHumidity, AvgPressure, AvgCloud, RainToday]]))[0])
      }
      print(salida)
      return render(request, "home/index.html", context = salida)
    salida = salida.cleaned_data()
    salida = salida.save()

def exit(request):
  logout(request)
  return redirect('/')

def profile(request):
  return render(request, 'log/profile/index.html')

def log(request):
  return render(request, '/registration/login.html')