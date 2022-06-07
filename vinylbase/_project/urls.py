# ======================================================================================================================
#
#                                                   URLs module
#
# ======================================================================================================================

# This is the URLs module of the project. The URL patterns are defined here.
# IMPORTANT: the patterns specified here are meant to control the triggering of functions in views.py module!

# ======================================================================================================================
#                                                    Libraries
# ======================================================================================================================

from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# ======================================================================================================================
#                                                 1. URL patterns
# ======================================================================================================================

# Define the URLs
urlpatterns = [

    # URLs of Django admin
    path('admin/', admin.site.urls),

    # Definition of URLs of each app
    path('users/', include('users.urls')),
    path('vinyls/', include('vinyls.urls')),

]

# Add the static url to the main URLs
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
