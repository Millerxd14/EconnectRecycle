from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from canecas import views

# Create your models here.


class BroadcastNotification(models.Model):
    mensaje = models.TextField(max_length=255)
    broadcast_on = models.DateTimeField()
    send = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=25,default="0")
    class Meta():
        ordering = ['-broadcast_on']



@receiver(post_save, sender=BroadcastNotification)
def notification_handler(sender,instance, created,**kwargs):
    #call group_send function directly to send notifications or crear una tarea dinamica con celery pero no sé como hacer esa mondá
    if created:
        views.test_notification()

    