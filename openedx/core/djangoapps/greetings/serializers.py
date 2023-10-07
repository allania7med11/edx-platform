from rest_framework import serializers
from openedx.core.djangoapps.greetings.models import Greeting

class GreetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greeting
        fields = ['text']