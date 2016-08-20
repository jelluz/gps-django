from django.db import models

# Create your models here.

class Gps(models.Model):
    lat = models.FloatField(verbose_name="lattitude")
    lon = models.FloatField(verbose_name="longitude")