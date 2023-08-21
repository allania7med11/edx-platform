from django.apps import AppConfig
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from edx_django_utils.plugins import PluginSettings, PluginURLs

from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType


class GreetingConfig(AppConfig):
    name = 'openedx.core.djangoapps.greetings'
    verbose_name = "Greeting"

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: '',
                PluginURLs.REGEX: '^api/greetings/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        },
        PluginSettings.CONFIG: {
            ProjectType.LMS: {
                SettingsType.PRODUCTION: {PluginSettings.RELATIVE_PATH: 'settings.production'},
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: 'settings.common'},
            }
        }
    }
    
    def ready(self):
        # Custom initialization code here
        pass
