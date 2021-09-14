from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "<int:component_id>/", views.component_detail, name="component_detail"
    ),
]
