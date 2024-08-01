"""
URL patterns for the lettings app.

This module defines the URL patterns for the lettings app. It includes the following patterns:
- An empty path that maps to the index view.
- A path with a dynamic parameter 'letting_id' that maps to the letting view.

The 'app_name' variable is set to "lettings" to provide a namespace for the URLs.

"""
from django.urls import path

from lettings import views

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="lettings_index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
