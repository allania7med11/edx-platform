import logging
from django.conf import settings
from django.urls import reverse
from oauth2_provider.models import Application
from urllib.parse import urljoin
import requests

log = logging.getLogger(__name__)


def make_original_greeting_call(greeting):
    client_id = "call_original_greeting_endpoint"
    token = get_access_token(client_id)
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    url = urljoin(settings.LMS_ROOT_URL, reverse("greetings_create"))
    data = {"text": greeting}
    response = requests.post(url, json=data, headers=headers)

    return response


def get_access_token(client_id):
    application: Application = get_or_create_oauth2_confidential_application(
        client_id
    )
    token_url = urljoin(settings.LMS_ROOT_URL, "/oauth2/access_token")

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

def get_or_create_oauth2_confidential_application(client_id) -> Application:
    # Check if an application with the provided client_id already exists
    application, created = Application.objects.get_or_create(
        client_id=client_id,
        defaults={
            "name": client_id,
            "authorization_grant_type": "client-credentials",
            "client_type": "confidential",
        },  # No need to set client_secret here
    )
    return application