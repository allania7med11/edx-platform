import logging
from django.conf import settings
from django.urls import reverse
from urllib.parse import urljoin
import requests

log = logging.getLogger(__name__)


def make_original_greeting_call(access_token, greeting):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    url = urljoin(settings.LMS_ROOT_URL, reverse("greetings_create"))
    data = {"text": greeting}
    response = requests.post(url, json=data, headers=headers)

    return response