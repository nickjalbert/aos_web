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
    name = models.CharField(max_length=200, unique=True)
    component_type = models.CharField(max_length=2, choices=COMPONENT_TYPES)
    description = models.TextField()

    @property
    def is_environment(self):
        return self.component_type == Component.ENVIRONMENT

    @property
    def is_policy(self):
        return self.component_type == Component.POLICY

    @property
    def is_agent(self):
        return self.component_type == Component.AGENT

    @property
    def is_dataset(self):
        return self.component_type == Component.DATASET

    @property
    def is_trainer(self):
        return self.component_type == Component.TRAINER

    @property
    def component_type_text(self):
        return {
            Component.ENVIRONMENT: "Environment",
            Component.POLICY: "Policy",
            Component.AGENT: "Agent",
            Component.DATASET: "Dataset",
            Component.TRAINER: "Trainer",
        }[self.component_type]


class ComponentRelease(TimeStampedModel):
    component = models.ForeignKey(
        "Component", on_delete=models.CASCADE, related_name="releases"
    )
    name = models.CharField(max_length=200)
    git_hash = models.CharField(max_length=200)
    github_url = models.CharField(max_length=200)
    file_path = models.TextField()
    class_name = models.CharField(max_length=200)
    requirements_path = models.TextField()
