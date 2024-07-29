from django.urls import path
from .views import hello_world

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('', hello_world, name='root'),  # Новый маршрут для корневого URL
]