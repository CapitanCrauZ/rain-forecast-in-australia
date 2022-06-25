from math import fabs
from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=45, null=False, blank=False)
    lastname = models.CharField(max_length=45, null=False, blank=False)
    age = models.PositiveBigIntegerField()
    date = models.DateField()
    gender = models.CharField(max_length=20)