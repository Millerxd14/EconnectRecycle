from django.shortcuts import render,HttpResponse

# Create your views here.


from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_notification(id):

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'notification_broadcast',
        {
            "type": 'send_notification',
            "id_notificacion": id
        }
    )
    return HttpResponse("Entregado")
