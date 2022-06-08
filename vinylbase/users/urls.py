# ======================================================================================================================
#
#                                                   URLs module
#
# ======================================================================================================================

# This is the URLs module of the Users app. The URL patterns are defined here.
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

    # Signup operations
    path('signup/', views.user_signup_view, name='user_signup'),
    path('signup-success/', TemplateView.as_view(template_name='users/user_signup_success.html'),
         name='user_signup_success'),
    path('account-exists/', TemplateView.as_view(template_name='users/user_account_exists.html'),
         name='user_account_exists'),

    # Login/logout operations
    path('login/', views.user_login_view, name='user_login'),
    path('login-invalid/', TemplateView.as_view(template_name='users/user_login_invalid.html'),
         name='user_login_invalid'),
    path('logout/', views.user_logout_view, name='user_logout'),

    # Change password operations
    path('change-password/', views.user_change_password_view, name='user_change_password'),
    path('password-changed/', TemplateView.as_view(template_name='users/user_password_changed.html'),
         name='user_password_changed'),
    path('invalid-old-password/', TemplateView.as_view(template_name='users/user_invalid_old_password.html'),
         name='user_invalid_old_password'),

    # Profile retrieving operations
    path('profile/', views.user_retrieve_view, name='user_retrieve'),

    # Profile delete operations
    path('profile/delete/', views.user_delete_view, name='user_delete'),
    path('profile/delete-success/', TemplateView.as_view(template_name='users/user_delete_success.html'),
         name='user_delete_success'),

]
