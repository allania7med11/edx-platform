from django.contrib import admin
from .models import Greeting

class GreetingAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')

admin.site.register(Greeting, GreetingAdmin)