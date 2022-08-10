from asyncio.windows_events import NULL
from multiprocessing import parent_process
from django.db import models
from django.contrib.auth.models import User

class Caneca(models.Model):
    '''Caneca'''
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    mac = models.CharField(max_length=15)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    latitud = models.CharField(max_length=200)
    longitud = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=150)

    n_peticiones = models.BigIntegerField(default=0)
    
    metal       = models.IntegerField(default=0)   
    paper       = models.IntegerField(default=0)
    glass       = models.IntegerField(default=0)
    trash       = models.IntegerField(default=0)
    plastic     = models.IntegerField(default=0)
    cardboard   = models.IntegerField(default=0)


    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        ''' return tittle'''
        return '{}, proveniente de la mac {}'.format(self.name, self.mac)
