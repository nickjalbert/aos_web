from django.shortcuts import render

from registry.models import Component


def index(request):
    components = list(Component.objects.all())
    context = {
        "environments": [c for c in components if c.is_environment],
        "agents": [c for c in components if c.is_agent],
        "policies": [c for c in components if c.is_policy],
        "datasets": [c for c in components if c.is_dataset],
        "trainers": [c for c in components if c.is_trainer],
    }
    return render(request, "leaderboard/index.html", context)
