from gps.models import Gps
from rest_framework import serializers

class GpsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gps
        fields = ('lat','lon','timestamp')

