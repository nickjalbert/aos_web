from django.http import HttpResponse
from django.shortcuts import render

from .models import Agent
from .models import Environment


def index(request):
    return HttpResponse(
            "Hello, world. You're at the registry index."
            f"There are {Agent.objects.count()} Agents and "
            f"{Environment.objects.count()} Environments."
            )
