import geocoder

from django.db import models

# Create your models here.

mapbox_access_token = 'pk.eyJ1IjoiY3JhdXoiLCJhIjoiY2w0dzZjZWk5MjV4eTNqczg2bmIwazNoMCJ9.VaYyChMCUOnf5dJjUhDwDg'

class map(models.Model):
    address = models.TextField(max_length=50)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(map, self).save(*args, **kwargs)