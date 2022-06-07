# ======================================================================================================================
#
#                                                  Forms module
#
# ======================================================================================================================

# This is the Forms module of the Vinyls app. These are loaded by the functions in the views.py module.

# ======================================================================================================================
#                                                    Libraries
# ======================================================================================================================

from django import forms
from .models import Vinyl, Genre

# ======================================================================================================================
#                                      1. User signup/authorization forms
# ======================================================================================================================


class VinylCreateForm(forms.ModelForm):
    """
    Form for creating a new Vinyl.
    """

    # General fields
    album = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=100)
    label = forms.CharField(max_length=100)
    original_year = forms.IntegerField(required=False)
    no_songs = forms.IntegerField(required=False)
    description = forms.CharField(required=False)
    edition_choices = [('O', 'Original'), ('RE', 'Reissue')]
    edition = forms.ChoiceField(required=False, choices=edition_choices)
    condition_choices = [('M', 'Mint'), ('NM', 'Near-Mint'), ('VG', 'Very-Good'), ('G', 'Good'), ('P', 'Poor')]
    condition = forms.ChoiceField(required=False, choices=condition_choices)
    cover = forms.ImageField(required=False)

    # Relational fields
    genre = forms.ModelMultipleChoiceField(required=False, queryset=Genre.objects.all())

    class Meta:
        model = Vinyl
        exclude = ('owner', 'submission_date')
