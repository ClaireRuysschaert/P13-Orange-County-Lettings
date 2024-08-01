"""
This module contains the admin configuration for managing profile data.

It registers the Profile model with the Django admin interface. This allows administrators to
manage Profile data directly through the Django admin site.

Registered Models:
- Profile: Represents a user profile with his favorite place.

Note:
By using admin.site.register, administrators can access the default admin interface for managing
the registered models. Additional customization of the admin interface can be achieved by
creating ModelAdmin subclasses and registering them instead.

Parameters:
- admin: Django admin module for managing the administrative interface of a Django project.
"""

from django.contrib import admin

from profiles.models import Profile

admin.site.register(Profile)
