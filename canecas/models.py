from asyncio.windows_events import NULL
from datetime import date
from multiprocessing import parent_process
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from notifications_app.models import BroadcastNotification
from datetime import datetime



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


@receiver(post_save, sender=Caneca)
def notification_handler(sender,instance, created,**kwargs):
    #call group_send function directly to send notifications or crear una tarea dinamica con celery pero no sé como hacer esa mondá
    caneca = instance
    usuario_defatult = instance.user
    # datetime object containing current date and time
    now = datetime.now()
    if(caneca.cardboard >= 80 ):
        mensaje = f"Tu caneca está llenandose de cartón, tiene {caneca.cardboard}%"
        notificacion = BroadcastNotification(
            mensaje = mensaje, 
            estado = 0, 
            broadcast_on= now.strftime("%Y-%m-%d %H:%M:%S"), 
            usuario_propietario = usuario_defatult, 
            usuario_enviador=usuario_defatult,
            direccion = 'canecas:consultas'
        )
        notificacion.save()
    if(caneca.glass >= 80 ):
        mensaje = f"Tu caneca está llenandose de vidrio, tiene {caneca.glass}%"
        notificacion = BroadcastNotification(
            mensaje = mensaje, 
            estado = 0, 
            broadcast_on= now.strftime("%Y-%m-%d %H:%M:%S"), 
            usuario_propietario = usuario_defatult, 
            usuario_enviador=usuario_defatult,
            direccion = 'canecas:consultas'
        )
        notificacion.save()
    if(caneca.metal >= 80 ):
        mensaje = f"Tu caneca está llenandose de metal, tiene {caneca.metal}%"
        notificacion = BroadcastNotification(
            mensaje = mensaje, 
            estado = 0, 
            broadcast_on= now.strftime("%Y-%m-%d %H:%M:%S"), 
            usuario_propietario = usuario_defatult, 
            usuario_enviador=usuario_defatult,
            direccion = 'canecas:consultas'
        )
        notificacion.save()
    if(caneca.paper >= 80 ):
        mensaje = f"Tu caneca está llenandose de papel, tiene {caneca.paper}%"
        notificacion = BroadcastNotification(
            mensaje = mensaje, 
            estado = 0, 
            broadcast_on= now.strftime("%Y-%m-%d %H:%M:%S"), 
            usuario_propietario = usuario_defatult, 
            usuario_enviador=usuario_defatult,
            direccion = 'canecas:consultas'
        )
        notificacion.save()
    if(caneca.plastic >= 80 ):
        mensaje = f"Tu caneca está llenandose de plastico, tiene {caneca.plastic}%"
        notificacion = BroadcastNotification(
            mensaje = mensaje, 
            estado = 0, 
            broadcast_on= now.strftime("%Y-%m-%d %H:%M:%S"), 
            usuario_propietario = usuario_defatult, 
            usuario_enviador=usuario_defatult,
            direccion = 'canecas:consultas'
        )
        notificacion.save()
    if(caneca.trash >= 80 ):
        mensaje = f"Tu caneca está llenandose de basura, tiene {caneca.trash}%"
        notificacion = BroadcastNotification(
            mensaje = mensaje, 
            estado = 0, 
            broadcast_on= now.strftime("%Y-%m-%d %H:%M:%S"), 
            usuario_propietario = usuario_defatult, 
            usuario_enviador=usuario_defatult,
            direccion = 'canecas:consultas'
        )
        notificacion.save()

