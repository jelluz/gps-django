from django.db import models

# Create your models here.

class Gps(models.Model):
    timestamp = models.TimeField(auto_now=True)
    lat = models.FloatField(verbose_name="lattitude")
    lon = models.FloatField(verbose_name="longitude")