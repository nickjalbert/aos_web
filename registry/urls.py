from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/components/", views.api_components, name="api_components"),
    path("api/runs/", views.api_runs, name="api_runs"),
    path(
        "api/runs/<int:run_id>/tarball",
        views.api_tarballs,
        name="api_tarballs",
    ),
    path(
        "<int:component_id>/", views.component_detail, name="component_detail"
    ),
]
