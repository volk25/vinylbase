# ======================================================================================================================
#
#                                                  Views module
#
# ======================================================================================================================

# This is the Views module of the Vinyls app. The template-rendering functions taking input from URLs and rendering
# template files are defined here.
# IMPORTANT: route the triggering of these functions in the urls.py module!
# (it's a good convention to name the template-triggering functions as the name of the template HTML file)

# ======================================================================================================================
#                                                    Libraries
# ======================================================================================================================

from django.shortcuts import render, redirect
from django.http import Http404
from .models import Vinyl
from .forms import VinylCreateForm

# ======================================================================================================================
#                                           1. Vinyl list/retrieve views
# ======================================================================================================================


def vinyl_list_view(request):
    """
    Function responsible for rendering the home template (passing data to the template and loading it to the page)
    """
    vinyls = Vinyl.objects.filter(owner=request.user)
    return render(request, 'vinyls/vinyl_list.html', {'vinyls': vinyls})


def vinyl_retrieve_view(request, vinyl_id: int):
    """
    Function responsible for rendering the vinyl details template (passing data to the template and loading it to the
    page)
    """
    try:
        vinyl = Vinyl.objects.get(owner=request.user, id=vinyl_id)
    except Vinyl.DoesNotExist:
        raise Http404('Vinyl not found')
    return render(request, 'vinyls/vinyl_retrieve.html', {'vinyl': vinyl})


def vinyl_create_view(request):
    """
    Vinyl create view.
    """

    # In case of POST request, instantiate the signup form
    if request.method == "POST":
        form = VinylCreateForm(request.POST, request.FILES)
        if form.is_valid():

            # Save the new vinyl and set the owner
            vinyl = form.save(commit=False)
            vinyl.owner = request.user
            vinyl.save()

            # Render the template and expose to it the queryset
            return redirect('vinyl_create_success')

    else:
        form = VinylCreateForm()

    # Render the template and expose to it the queryset
    return render(request, 'vinyls/vinyl_create.html', {'form': form})