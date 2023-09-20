"""Core app."""

# Django
from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Core config class."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
