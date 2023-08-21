import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from openedx.core.djangoapps.greetings.models import Greeting
from openedx.core.djangoapps.greetings.serializers import GreetingSerializer

from openedx.core.lib.api.authentication import BearerAuthentication


log = logging.getLogger(__name__)

class GreetingsCreateView(APIView):
    authentication_classes = (JwtAuthentication, BearerAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = GreetingSerializer(data=request.data)
        if serializer.is_valid():
            greeting: Greeting  = serializer.save()
            log.info(f"Greeting {greeting.text} at {greeting.created_at}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    