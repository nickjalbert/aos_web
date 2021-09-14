from django.http import HttpResponse
from django.shortcuts import render  # noqa: F401
from django.shortcuts import get_object_or_404

import yaml

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


def api_components(request):
    all_components = {}
    for component in Component.objects.all():
        releases = []
        component_data = {
            "type": component.component_type_text.lower(),
            "description": component.description,
            "releases": releases,
        }
        for release in component.releases.all():
            release_data = {
                "name": release.name,
                "hash": release.git_hash,
                "github_url": release.github_url,
                "file_path": release.file_path,
                "class_name": release.class_name,
                "requirements_path": release.requirements_path,
            }
            releases.append(release_data)
        all_components[component.name] = component_data
    return HttpResponse(yaml.dump(all_components))
