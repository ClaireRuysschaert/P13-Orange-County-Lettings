"""
Views for handling user profiles in the profiles app.

This module defines views for processing HTTP requests related to :class:`profiles.Profile` in the
profiles app of the project.

Defined views include:
    - index: Renders the profiles index page, showing a list of all :class:`profiles.Profile`.
    - profile: Renders the details page for a specific :class:`profiles.Profile` identified by
      profile ID.

Usage:
    These views display information about :class:`profiles.Profile`, such as usernames, favorite
    cities, or other profile-related data. They interact with the :class:`profiles.Profile` model
    to fetch data from the database and render it in the appropriate templates.

:param render: A module to render templates in Django views.
:param get_object_or_404: A function provided by Django that retrieves an object from the database
    or raises a Http404 exception if the object does not exist.
"""
from http.client import HTTPResponse
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
import sentry_sdk
from profiles.models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed
# consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d
def index(request: HttpRequest) -> HTTPResponse:
    """
    View function for the index page of the profiles app.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HTTPResponse: The HTTP response object containing the rendered index.html template.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        return render(request, "profiles/index.html", context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        raise


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque
# quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus, it. Nam aliquam
# dignissim congue. Pellentesque habitant morbi tristique senectus et netus et
# males
def profile(request: HttpRequest, profile_id: int) -> HTTPResponse:
    """
    View function to display a user profile.

    Args:
        request (HttpRequest): The HTTP request object.
        profile_id (int): The ID of the profile to be displayed.

    Returns:
        HTTPResponse: The HTTP response containing the rendered profile template.
    """
    try:
        profile = get_object_or_404(Profile, pk=profile_id)
        context = {"profile": profile}
        return render(request, "profile.html", context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        raise
