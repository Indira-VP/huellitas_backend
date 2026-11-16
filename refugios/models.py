from django.db import models


class Refugio(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
