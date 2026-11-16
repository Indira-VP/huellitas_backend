from rest_framework import serializers

from .models import Mascota


class MascotaSerializer(serializers.ModelSerializer):
    refugio_nombre = serializers.CharField(
        source='refugio.nombre',
        read_only=True,
        allow_null=True,
    )

    class Meta:
        model = Mascota
        fields = [
            'id',
            'nombre',
            'especie',
            'raza',
            'edad',
            'estado',
            'descripcion',
            'refugio',
            'refugio_nombre',
        ]
