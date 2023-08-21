from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from openedx.core.djangoapps.greeting.models import Greeting

class GreetingView(APIView):
    authentication_classes = [OAuth2Authentication]
    
    def post(self, request):
        greeting_text = request.data.get('greeting')
        print(f"Received greeting: {greeting_text}")
        Greeting.objects.create(text=greeting_text)
        response_data = {"message": "Greeting received and logged."}
        return Response(response_data, status=status.HTTP_201_CREATED)