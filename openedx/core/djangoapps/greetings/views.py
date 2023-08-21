from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from openedx.core.lib.api.authentication import BearerAuthentication


class GreetingsCreateView(APIView):
    authentication_classes = (JwtAuthentication, BearerAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        """
        Handle GET requests.
        """
        data = {"message": "This is a GET request!"}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST requests.
        """
        data = {"message": "This is a POST request!"}
        return Response(data, status=status.HTTP_201_CREATED)
    

    