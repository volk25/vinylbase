# ======================================================================================================================
#
#                                                  Models module
#
# ======================================================================================================================

# This is the Models module of the Vinyls app. The classes used for building the migrations are defined here.
# It is good to start building the project from this module.
# IMPORTANT: After modifying these, the migrations have to be recreated (the SQL database will be also generated).

# ======================================================================================================================
#                                                    Libraries
# ======================================================================================================================

from django.db import models
from django.contrib.auth.models import User

# ======================================================================================================================
#                              1. Data for constructing the database scheme and queries
# ======================================================================================================================


class Genre(models.Model):
    """
    The Genre names for the genre field will be taken from this class
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vinyl(models.Model):
    """
    Create the fields to be filled in for each vinyl
    """

    # General fields
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    original_year = models.IntegerField(null=True, blank=True)
    no_songs = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    edition_choices = [('O', 'Original'), ('RE', 'Reissue')]
    edition = models.CharField(max_length=2, choices=edition_choices, blank=True, null=True)
    condition_choices = [('M', 'Mint'), ('NM', 'Near-Mint'), ('VG', 'Very-Good'), ('G', 'Good'), ('P', 'Poor')]
    condition = models.CharField(max_length=2, choices=condition_choices, blank=True, null=True)
    submission_date = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to="images/", null=True, blank=True)

    # Relational fields
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, blank=True, null=True)

    def __str__(self):
        return self.album



