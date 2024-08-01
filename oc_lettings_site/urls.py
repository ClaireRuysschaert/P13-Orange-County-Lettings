from django.contrib import admin
from django.urls import path, include
from . import views

"""
This module contains the URL configuration for the project.

It defines the top-level URL patterns for the project, including the URL patterns for the
Django admin interface and the URL patterns from various apps within the project.

The patterns defined here include:
- /admin/ - URL pattern for accessing the Django admin interface.
- /lettings/ and /profiles/ - URL patterns included from the 'lettings' and 'profiles' apps.
- /trigger-error/ - URL pattern for triggering a 500 server error for testing purposes.

Notes:
- The URL patterns for individual apps are included using the 'include' function, which allows
for modular and organized URL configuration.
- Each app's URL patterns are namespaced to prevent naming conflicts and provide better
organization and readability.

Parameters:
- admin: The instance of the Django admin site.
- path: The function used for defining URL patterns.
- include: The function used for including URL patterns from other apps.
"""

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('trigger-error/', views.trigger_error_500),
]
