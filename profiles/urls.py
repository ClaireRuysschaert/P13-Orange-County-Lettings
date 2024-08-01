"""
URL Configuration for the profiles app.

This module specifies the URL patterns for the profiles app within the project. The profiles app
manages user profiles and their associated views.

Defined patterns include:
    - An empty path that maps to the profiles index page, displaying a list of all user profiles.
    - /<int:profile_id>/ - Route for viewing details of a specific user profile identified
      by the profile ID.

Notes:
    The URL patterns are namespaced under 'profiles' to avoid naming conflicts and enhance
    organization and readability. The views corresponding to these URL patterns are defined in the
    'views.py' module of the profiles app.

Usage:
    This file acts as the URL configuration for the profiles app. It includes routes for various
    profiles functionalities, such as listing all user profiles and viewing individual user
    profiles.

:param path: A module for defining URL patterns in Django projects.
"""
from django.urls import path

from profiles import views

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="profiles_index"),
    path("<int:profile_id>/", views.profile, name="profile"),
]
