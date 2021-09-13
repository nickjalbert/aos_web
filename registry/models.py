from django.db import models


class Environment(models.Model):
    name = models.CharField(max_length=200)


class Agent(models.Model):
    name = models.CharField(max_length=200)
