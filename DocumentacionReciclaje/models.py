from django.db import models

# Create your models here.


class Poster(models.Model):
    titulo = models.CharField(max_length=35)
    definicion = models.CharField(max_length=255)
    clasificacion = models.CharField(max_length=1200)
    recolector_disponible = models.BooleanField()

