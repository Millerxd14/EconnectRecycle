# chat/consumers.py
import json
import random
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import BroadcastNotification
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from django.core import serializers



class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #self.scope["session"]["seed"] = random.randint(1, 1000)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'notification_%s' % self.room_name

        print(self.room_group_name)
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']

    #     # Send message to room group
    #     await self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )

    # Receive message from room group
    async def send_notification(self, event):
        #message = event['message']
        message = "La asincronia se la come entera"
        
        notificaciones = await database_sync_to_async(self.obtener_notificaciones_usuario)()

        await self.send(text_data=json.dumps({
            'message': notificaciones
        }))

    def obtener_notificaciones_usuario(self):
        usuario = User.objects.get(username = self.scope["user"])
        notificaciones = BroadcastNotification.objects.filter(usuario_id = usuario.id)
        return serializers.serialize("json", notificaciones,fields=('mensaje','estado'))