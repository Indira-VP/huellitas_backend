from django.db import models


class Mascota(models.Model):
    ESPECIES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Otro', 'Otro'),
    ]

    ESTADOS = [
        ('Disponible', 'Disponible'),
        ('En adopción', 'En adopción'),
        ('Adoptada', 'Adoptada'),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=20, choices=ESPECIES)
    raza = models.CharField(max_length=100, blank=True)
    edad = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Disponible')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

# Create your models here.
