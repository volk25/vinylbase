# ======================================================================================================================
#
#                                                  Models module
#
# ======================================================================================================================

# This is the Models module of the project. The classes used for building the migrations are defined here.
# It is good to start building the project from this module.
# IMPORTANT: After modifying these, the migrations have to be recreated (the SQL database will be also generated).

# ======================================================================================================================
#                                                    Libraries
# ======================================================================================================================

from django.db import models

# ======================================================================================================================
#                              1. Data for constructing the database scheme and queries
# ======================================================================================================================


class Vinyl(models.Model):
    """
    Create the fields to be filled in for each vinyl
    Input:
    None
    Output:
    - Fields are shown as ordered (the data for them should be in the SQL database)
    """

    # The album, artist and label are all character fields
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    label = models.CharField(max_length=100)

    # The original year and number of songs are integer fields
    original_year = models.IntegerField(null=True)
    no_songs = models.IntegerField(null=True)

    # The description is a test field
    description = models.TextField(null=True)

    # The edition of the vinyl should be chosen between some options
    edition_choices = [('O', 'Original'), ('RE', 'Reissue')]
    edition = models.CharField(max_length=2, choices=edition_choices, blank=True)

    # The condition of the vinyl should be chosen between some options
    condition_choices = [('M', 'Mint'), ('NM', 'Near-Mint'), ('VG', 'Very-Good'), ('G', 'Good'), ('P', 'Poor')]
    condition = models.CharField(max_length=2, choices=condition_choices, blank=True)

    # The submission date field should be a datetime field
    submission_date = models.DateTimeField()

    # The cover picture is an image field
    cover = models.ImageField(upload_to="images/", null=True, blank=True)

    # The genre field is a many-to-many field and a class should be passed to it
    genre = models.ManyToManyField('Genre', blank=True)

    # We want to display the pets names (and not the objects with theirs IDs) in the admin form (dunder str method)
    def __str__(self):
        return self.album


class Genre(models.Model):
    """
    The Genre names for the genre field will be taken from this class
    Input:
    None
    Output:
    - Fields are shown as ordered (the data for them should be in the SQL database)
    """

    # The name of the genre is a character field
    name = models.CharField(max_length=50)

    # We want to display the genre names (and not the objects with theirs IDs) in the admin form (dunder str method)
    def __str__(self):
        return self.name
