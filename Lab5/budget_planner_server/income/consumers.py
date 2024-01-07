import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)  # Set up a logger for this module

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("WebSocket connected")
        # Add this socket to the income_updates group
        await self.channel_layer.group_add(
            "income_updates",  # Group name
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        logger.info(f"WebSocket disconnected with code: {close_code}")
        # Remove this socket from the income_updates group on disconnect
        await self.channel_layer.group_discard(
            "income_updates",
            self.channel_name
        )

    async def income_update(self, event):
        logger.info(f"Sending income update: {event}")
        # Send a message to this WebSocket
        try:
            await self.send(text_data=json.dumps({
                'action': event.get("action"),  # e.g., "created", "updated", "deleted"
                'income': event.get("income"),  # The income data, ensure this is serializable
            }))
        except Exception as e:
            logger.error(f"Error sending message: {e}")
