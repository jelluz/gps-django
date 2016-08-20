from django.shortcuts import render

# Create your views here.
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from gps.serializers import GpsSerializer
from gps.models import Gps


class GpsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Gps.objects.all().order_by('-timestamp')
    serializer_class = GpsSerializer

