"""Django admin customization."""

# Django
from django.contrib import admin
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from core.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for the custom user model."""

    ordering = ["id"]
    list_display = ["email", "name"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name",)}),
        (_("Permissions"), {
            "fields": ("is_active", "is_staff", "is_superuser")
        }),
        (_("Important dates"), {"fields": ("last_login",)}),
    )

    readonly_fields = ["last_login"]

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "name",
                "is_active",
                "is_staff",
                "is_superuser",
            ),
        }),
    )
