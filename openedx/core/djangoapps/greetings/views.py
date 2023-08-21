from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from openedx.core.djangoapps.greetings.models import Greeting
from openedx.core.lib.api.authentication import BearerAuthentication
from rest_framework import permissions


class GreetingsCreateView(CreateAPIView, APIView):
    authentication_classes = (BearerAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request):
        greeting_text = request.data.get('greetings')
        print(f"Received greeting: {greeting_text}")
        Greeting.objects.create(text=greeting_text)
        response_data = {"message": "Greeting received and logged."}
        return Response(response_data, status=status.HTTP_201_CREATED)