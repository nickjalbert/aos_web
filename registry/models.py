from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Component(TimeStampedModel):
    ENVIRONMENT = "EN"
    POLICY = "PO"
    AGENT = "AG"
    DATASET = "DA"
    TRAINER = "TR"
    COMPONENT_TYPES = [
        (ENVIRONMENT, "EN"),
        (POLICY, "PO"),
        (AGENT, "AG"),
        (DATASET, "DA"),
        (TRAINER, "TR"),
    ]
    name = models.CharField(max_length=200)
    component_type = models.CharField(max_length=2, choices=COMPONENT_TYPES)
    description = models.TextField()


class ComponentRelease(TimeStampedModel):
    component = models.ForeignKey("Component", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    git_hash = models.CharField(max_length=200)
    github_url = models.CharField(max_length=200)
    file_path = models.TextField()
    class_name = models.CharField(max_length=200)
    requirements_path = models.TextField()
