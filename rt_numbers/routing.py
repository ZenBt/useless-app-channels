from django.urls import path

from .consumers import NumbersConsumer

ws_urlpatterns = [
    path('numbers', NumbersConsumer.as_asgi())
]