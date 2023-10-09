from django.apps import AppConfig
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from edx_django_utils.plugins import PluginSettings, PluginURLs

from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType


class GreetingConfig(AppConfig):
    name = 'openedx.core.djangoapps.greetings'
    verbose_name = "Greeting"
