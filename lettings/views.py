"""
Views for managing letting properties in the lettings app.

This module contains views for handling HTTP requests related to letting properties in the lettings
app of the project.

Views:
    - index: Renders the lettings index page, displaying a list of all letting properties.
    - letting: Renders the details page for a specific letting property identified by its ID.

Usage:
    These views can be used to display information about letting properties, including their titles
    and addresses. They interact with the Letting model to retrieve data from the database and
    render it in the appropriate templates.

:param Letting: Represents a letting (rental) property in the database.
:type Letting: class:`lettings.Letting`
:param render: A module used to render templates in Django views.
:param get_object_or_404: A function provided by Django that retrieves an object from the database
or raises a Http404 exception if the object does not exist.
"""
from http.client import HTTPResponse
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
import sentry_sdk
from lettings.models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat
# massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu. Vestibulum ante ipsum primis
# in faucibus orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request: HttpRequest) -> HTTPResponse:
    """
    View function for the index page.

    Retrieves all the lettings from the database and renders them on the index page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HTTPResponse: The HTTP response object containing the rendered index page.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {"lettings_list": lettings_list}
        return render(request, "lettings/index.html", context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        raise


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae
# efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est
# ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse
# potenti. In tempus a nisi sed laoreet. Suspendisse porta dui eget sem accumsan interdum. Ut
# quis urna pellentesque justo mattis ullamcorper ac non tellus. In tristique mauris eu velit
# fermentum, tempus pharetra est luctus. Vivamus consequat aliquam libero, eget bibendum lorem.
# Sed non dolor risus. Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer
# vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request: HttpRequest, letting_id: int) -> HTTPResponse:
    """
    View function for displaying a letting detail.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to be displayed.

    Returns:
        HTTPResponse: The HTTP response object containing the rendered letting.html template.
    """
    try:
        letting = get_object_or_404(Letting, pk=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "letting.html", context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        raise
