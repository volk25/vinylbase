from django.contrib import admin
from .models import Vinyl


@admin.register(Vinyl)
class VinylAdmin(admin.ModelAdmin):
    list_display = ['album', 'artist', 'label', 'original_year', 'edition', 'condition']
