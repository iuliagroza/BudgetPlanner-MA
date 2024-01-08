import json

from channels.generic.websocket import AsyncWebsocketConsumer


class IncomeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add('income_updates', self.channel_name)

    async def disconnect(self, close_code):
        pass

    async def send_income_update(self, event):
        await self.send(text_data=json.dumps(event['data']))