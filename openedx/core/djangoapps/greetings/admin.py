from django.contrib import admin
from openedx.core.djangoapps.greetings.models import Greeting

class GreetingAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')

admin.site.register(Greeting, GreetingAdmin)