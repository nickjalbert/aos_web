from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/components/", views.api_components, name="api_components"),
    path(
        "<int:component_id>/", views.component_detail, name="component_detail"
    ),
]
