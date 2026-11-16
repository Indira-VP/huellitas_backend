from rest_framework import serializers

from .models import Refugio


class RefugioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refugio
        fields = ['id', 'nombre', 'direccion', 'telefono']
