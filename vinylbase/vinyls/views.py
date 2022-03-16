# ======================================================================================================================
#
#                                                  Views module
#
# ======================================================================================================================

# This is the Views module of the project. The template-rendering functions taking input from URLs and rendering
# template files are defined here.
# IMPORTANT: route the triggering of these functions in the urls.py module!
# (it's a good convention to name the template-triggering functions as the name of the template HTML file)

# ======================================================================================================================
#                                                    Libraries
# ======================================================================================================================

from django.shortcuts import render
from django.http import Http404
from .models import Vinyl

# ======================================================================================================================
#                                           1. Template-rendering functions
# ======================================================================================================================


def home(request):
    """
    Function responsible for rendering the home template (passing data to the template and loading it to the page)
    Input:
    - http request
    Output:
    - Renders the home.html template
    """

    # Get all the vinyl objects
    vinyls = Vinyl.objects.all()

    # Define a dictionary with data that should be available inside of the template
    vinyls_dict = {
        'vinyls': vinyls
    }

    # Return the render function
    return render(request, 'home.html', vinyls_dict)


def details(request, vinyl_id: int):
    """
    Function responsible for rendering the vinyl details template (passing data to the template and loading it to the
    page)
    Input:
    - http request
    - vinyl_id(int): id of the desired vinyl
    Output:
    - Renders the details.html template
    """

    # Get the requested vinyl object
    try:
        vinyl = Vinyl.objects.get(id=vinyl_id)
    except Vinyl.DoesNotExist:
        raise Http404('Vinyl not found')

    # Define a dictionary with data that should be available inside of the template
    vinyl = {
        'vinyl': vinyl
    }

    # Return the render function
    return render(request, 'details.html', vinyl)

