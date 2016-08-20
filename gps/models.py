from django.db import models

# Create your models here.

class Gps(models.Model):
    timestamp = models.DateTimeField(auto_now=True, verbose_name="timestamp")
    lat = models.FloatField(verbose_name="lattitude")
    lon = models.FloatField(verbose_name="longitude")