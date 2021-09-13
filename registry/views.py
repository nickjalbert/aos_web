from django.http import HttpResponse
from django.shortcuts import render  # noqa: F401

from .models import Component
from .models import ComponentRelease


def index(request):
    return HttpResponse(
        "Hello, world. You're at the registry index."
        f"There are {Component.objects.count()} Components with "
        f"{ComponentRelease.objects.count()} releases."
    )
