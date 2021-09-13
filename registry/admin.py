from django.contrib import admin

from .models import Environment, Agent

admin.site.register(Environment)
admin.site.register(Agent)
