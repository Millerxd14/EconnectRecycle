from django.db import models


class Caneca(models.Model):
    '''Caneca'''
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    mac = models.CharField(max_length=15)
    
    
    latitud = models.CharField(max_length=200)
    longitud = models.CharField(max_length=200)

    ubicacion = models.CharField(max_length=150)


    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        ''' return tittle'''
        return '{}, proveniente de la mac {}'.format(self.name, self.mac)
