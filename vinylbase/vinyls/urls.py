# ======================================================================================================================
#
#                                                   URLs module
#
# ======================================================================================================================

# This is the URLs module of the Vinyls app. The URL patterns are defined here.
# IMPORTANT: the patterns specified here are meant to control the triggering of actions in views.py module of the
# current app!

# ======================================================================================================================
#                                                    Libraries
# ======================================================================================================================

from django.views.generic import TemplateView
from django.urls import path
from . import views

# ======================================================================================================================
#                                               1. URL patterns
# ======================================================================================================================

urlpatterns = [
    path('', views.vinyl_list_view, name='vinyl_list'),
    path('create/', views.vinyl_create_view, name='vinyl_create'),
    path('create-success/', TemplateView.as_view(template_name='vinyls/vinyl_create_success.html'),
         name='vinyl_create_success'),
    path('<int:vinyl_id>/', views.vinyl_retrieve_view, name='vinyl_retrieve'),
]
