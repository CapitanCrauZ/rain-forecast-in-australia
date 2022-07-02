from email.headerregistry import Address
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.views.generic.edit import CreateView
from matplotlib.style import context
from .models import map

# def map(request):
#     mapbox_access_token = 'pk.my_mapbox_access_token'
#     return render(request, 'map/map.html', {
#         'mapbox_access_token': mapbox_access_token
#     })

class MapView(CreateView):

        model = map
        fields = ['address']
        template_name = 'map/map.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['mapbox_access_token'] = 'pk.eyJ1IjoiY3JhdXoiLCJhIjoiY2w0dzZjZWk5MjV4eTNqczg2bmIwazNoMCJ9.VaYyChMCUOnf5dJjUhDwDg'
            context['addresses'] = map.objects.all()
            return context