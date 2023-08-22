import logging
import random
import string
from django.urls import reverse
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from openedx.core.djangoapps.greetings.models import Greeting
from openedx.core.djangoapps.greetings.serializers import GreetingSerializer
from oauth2_provider.models import Application

from openedx.core.lib.api.authentication import BearerAuthentication


log = logging.getLogger(__name__)


class GreetingsCreateView(APIView):
    authentication_classes = (
        JwtAuthentication,
        BearerAuthentication,
        SessionAuthentication,
    )
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = GreetingSerializer(data=request.data)
        if serializer.is_valid():
            greeting: Greeting = serializer.save()
            log.info(f"Greeting {greeting.text} at {greeting.created_at}")
            if greeting.text == "hello":
                return self.make_original_greeting_call("goodbye")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def make_original_greeting_call(self, greeting):
        token = self.get_oauth2_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        url = self.get_greetings_create_url()
        data = {"text": greeting}
        response = requests.post(url, json=data, headers=headers)

        return response

    def get_oauth2_token(self):
        client_id = "call_original_greeting_endpoint"
        application: Application = self.get_or_create_oauth2_confidential_application(
            client_id
        )
        token_url = self.get_token_url()

        # Set up the request data
        data = {
            "grant_type": "client_credentials",
            "client_id": application.client_id,
            "client_secret": application.client_secret,
        }
        try:
            # Make the HTTP POST request to the token endpoint
            response = requests.post(token_url, data=data)

            # Check if the request was successful
            if response.status_code == 200:
                token_data = response.json()
                return token_data.get("access_token")
            else:
                log.error(
                    f"Token request failed with status code {response.status_code}: {response.text}"
                )
                return None

        except Exception as e:
            log.error(f"Token request encountered an error: {str(e)}")
            return None

    def get_or_create_oauth2_confidential_application(self, client_id) -> Application:
        # Check if an application with the provided client_id already exists
        application, created = Application.objects.get_or_create(
            client_id=client_id,
            defaults={
                "authorization_grant_type": "client-credentials",
                "client_type": "confidential",
            },  # No need to set client_secret here
        )

        if created:
            # Generate and assign a random client_secret for the newly created application
            client_secret = self.generate_random_client_secret()
            application.client_secret = client_secret
            application.save()
        return application

    def generate_random_client_secret(self, length=32):
        characters = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choice(characters) for _ in range(length))
    
    def get_token_url(self):
        token_url = reverse("oauth2_provider:token")
        return self.request.build_absolute_uri(token_url)

    def get_greetings_create_url(self):
        greetings_create_url = reverse("greetings_create")
        return self.request.build_absolute_uri(greetings_create_url)

    
