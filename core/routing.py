from django.urls import path
from .consumers import YourConsumer

websocket_urlpatterns = [
    path("ws/path", YourConsumer.as_asgi()),
]
