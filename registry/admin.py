from django.contrib import admin

from .models import Component, ComponentRelease

admin.site.register(Component)
admin.site.register(ComponentRelease)
