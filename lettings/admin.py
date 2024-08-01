"""
This module contains the admin configuration for managing Lettings data.

It registers the Lettings models (Address and Letting) with the Django admin interface. This allows
administrators to manage Lettings data directly through the Django admin site.

Registered Models:
- Address: Represents an address associated with a letting.
- Letting: Represents a letting, including the address and title.

Note:
By using admin.site.register, administrators can access the default admin interface for managing
the registered models. Additional customization of the admin interface can be achieved by
creating ModelAdmin subclasses and registering them instead.

Parameters:
- admin: Django admin module for managing the administrative interface of a Django project.
"""

from django.contrib import admin

from lettings.models import Address, Letting

admin.site.register(Address)
admin.site.register(Letting)
