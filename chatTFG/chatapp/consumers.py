# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async,SyncToAsync
from .models import Mensajes,Salas


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_user = self.scope['user'].username
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def save_message(self, message):
        user = self.scope['user']
        sala = Salas.objects.get(id=self.room_name)
        mensaje = Mensajes(user=user, sala=sala, mensaje=message)
        mensaje.save()
        
    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.save_message(message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message,'nameUser':self.room_user,}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        nameUser=event['nameUser']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message,'nameUser':nameUser}))