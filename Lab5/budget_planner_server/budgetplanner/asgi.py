"""
ASGI config for budgetplanner project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import income.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "budgetplanner.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Define WebSocket protocol
    "websocket": AuthMiddlewareStack(
        URLRouter(
            income.routing.websocket_urlpatterns  # Define WebSocket URL routing
        )
    ),
})
