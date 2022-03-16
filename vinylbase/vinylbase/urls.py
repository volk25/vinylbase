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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from vinyls import views  #for these is fine to be unresolved (since the system doesn't see the apps sometimes)

# ======================================================================================================================
#                                                 1. URL patterns
# ======================================================================================================================

"""
In the following 'urlpatterns' list all the paths should be listed.
In the path function:
- 1st argument: URL
- 2nd argument: function in the views.py to be called
- 3rd argument: name of the page to be displayed 
Error 404 will be rendered if the inputted URL will not correspond to any of the defined in the paths.
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('vinyls/<int:vinyl_id>/', views.details, name='details'),
    # Add here more paths
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
