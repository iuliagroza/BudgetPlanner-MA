from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Income  
import logging

logger = logging.getLogger(__name__)  # Set up a logger for this module

@receiver(post_save, sender=Income)
def announce_new_income(sender, instance, created, **kwargs):
    if created:
        logger.info(f"New income created: {instance}")
    else:
        logger.info(f"Income updated: {instance}")
    channel_layer = get_channel_layer()
    message = {
        "type": "income.update",  # corresponds to the method in the consumer
        "action": "created" if created else "updated",
        "income": {
            "id": str(instance.id),  
            "amount": instance.amount,  
            "date": instance.date.isoformat(),  
            "category": instance.category,  
            "note": instance.note
        }
    }
    async_to_sync(channel_layer.group_send)("income_updates", message)

@receiver(post_delete, sender=Income)
def announce_deleted_income(sender, instance, **kwargs):
    logger.info(f"Income deleted: {instance}")
    channel_layer = get_channel_layer()
    message = {
        "type": "income.update",
        "action": "deleted",
        "income": {
            "id": str(instance.id),  
            "amount": instance.amount,  
            "date": instance.date.isoformat(),  
            "category": instance.category,  
            "note": instance.note
        }
    }
    async_to_sync(channel_layer.group_send)("income_updates", message)
