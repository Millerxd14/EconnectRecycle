
from .models import Caneca
from rest_framework import serializers



class CanecaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Caneca
        fields = [
            'id',
            'name',
            'description',
            'mac', 
            'ubicacion',
            'latitud',
            'longitud',
            'cardboard',
            'glass',
            'metal',
            'paper',
            'plastic',
            'trash'
        ]
