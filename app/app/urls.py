"""URLs configuration for app project."""

# Django
from django.contrib import admin
from django.urls import path

# Third party libraries
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL for API documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs'
    )
]
