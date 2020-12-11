import json
from channels.generic.websocket import AsyncWebsocketConsumer

class Consumer(AsyncWebsocketConsumer):

    room_name = None
    room_group_name = none

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # join the group
        async self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        #Leave room group
        if self.room_group_name and self.channel_name:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
    async def receive(self, text_data=None, bytes_data=None):
        event = json.loads(text_data)
        message = event['message']

        #send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
            'type' = 'chat_message',
            'username' : self.scope['user'].username.title(),
            'message' : message


            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        #send back this message
        await self.send(text_data=json.dumps({
            'message' : message,
            'username' : username
        }))
