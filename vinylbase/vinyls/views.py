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
    Function responsible for rendering the vinyl list template.
    """
    if not request.user.is_anonymous:
        vinyl_qs = Vinyl.objects.filter(owner=request.user)
    else:
        return redirect('home')
    return render(request, 'vinyls/vinyl_list.html', {'vinyl_qs': vinyl_qs})


def vinyl_retrieve_view(request, vinyl_id: int):
    """
    Function responsible for rendering the vinyl details template.
    """
    if not request.user.is_anonymous:
        try:
            vinyl_obj = Vinyl.objects.get(owner=request.user, id=vinyl_id)
        except Vinyl.DoesNotExist:
            raise Http404('Vinyl not found')
    else:
        return redirect('home')
    return render(request, 'vinyls/vinyl_retrieve.html', {'vinyl_obj': vinyl_obj})


def vinyl_delete_view(request, vinyl_id: int):
    """
    Function responsible for deleting a vinyl.
    """
    try:
        vinyl = Vinyl.objects.get(owner=request.user, id=vinyl_id)
    except Vinyl.DoesNotExist:
        raise Http404('Vinyl not found')
    vinyl.delete()
    return redirect('vinyl_delete_success')


def vinyl_create_view(request):
    """
    Function responsible for rendering the vinyl create template.
    """

    # In case of POST request, create a new Vinyl instance
    if request.method == "POST":
        form = VinylCreateForm(request.POST, request.FILES)
        if form.is_valid():

            # Save the new vinyl and set the owner
            vinyl = form.save(commit=False)
            vinyl.owner = request.user
            vinyl.save()

            # Render the template and expose to it the queryset
            return redirect('vinyl_create_success')

    # In case of GET request, instantiate the form
    else:
        form = VinylCreateForm()

    # Render the template and expose to it the queryset
    return render(request, 'vinyls/vinyl_create.html', {'form': form})