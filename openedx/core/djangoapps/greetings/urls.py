from django.urls import path
from .views import GreetingsCreateView

urlpatterns = [
    path("", GreetingsCreateView.as_view(), name="greetings_create"),
]
