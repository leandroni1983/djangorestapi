import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from myapp.models import MyModel


@sync_to_async
def synchronous_operation():
    # perform blocking operation here
    return list(MyModel.objects.all().values())


class YourConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self, event):

        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self):
        data = await synchronous_operation()
        data_string = json.dumps(data)
        await self.send({
            "type": "websocket.send",
            "text": data_string,
        })

    async def websocket_disconnect(self, event):
        pass

    async def websocket_message(self, event):
        text_data_json = json.loads(event['text'])
        message = text_data_json["message"]
        await self.send({
            "type": "websocket.receive",
            "text": message,
        })
