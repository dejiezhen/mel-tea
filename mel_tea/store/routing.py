# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('chat/chatbox/', consumers.ChatConsumer.as_asgi()),
]