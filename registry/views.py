from django.http import HttpResponse
from django.shortcuts import render  # noqa: F401
from django.shortcuts import get_object_or_404

from .models import Component
from .models import ComponentRelease


def index(request):
    return HttpResponse(
        "Hello, world. You're at the registry index."
        f"There are {Component.objects.count()} Components with "
        f"{ComponentRelease.objects.count()} releases."
    )


def component_detail(request, component_id):
    component = get_object_or_404(Component, pk=component_id)
    context = {"component": component}
    return render(request, "registry/component_detail.html", context)
