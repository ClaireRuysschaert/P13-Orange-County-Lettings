from django.http import HttpResponse
from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis
# leo consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis,
# sem mi convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus
# ipsum, eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis
# tempus. Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
# pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna, non finibus
# neque cursus id.
def index(request) -> HttpResponse:
    """
    Renders the index.html template.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response.
    """
    return render(request, "index.html")


def trigger_error_500(request) -> HttpResponse:
    """
    Raises an exception to trigger a server error for testing purposes.

    Args:
        request (HttpRequest): The HTTP request object.

    Raises:
        Exception: An intentional exception to simulate a server error.

    Returns:
        HttpResponse: The HTTP response object.
    """
    raise Exception("Intentional server error for testing purposes")
