from django.urls import path
from .views import GreetingsCreateView

urlpatterns = [
    path("", GreetingsCreateView, name="greetings_create"),
]
