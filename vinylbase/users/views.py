# ======================================================================================================================
#
#                                                  Views module
#
# ======================================================================================================================

# This is the Views module of the Users app. The template-rendering functions taking input from URLs and rendering
# template files are defined here.
# IMPORTANT: route the triggering of these functions in the urls.py module!
# (it's a good convention to name the template-triggering functions as the name of the template HTML file)

# ======================================================================================================================
#                                                    Libraries
# ======================================================================================================================

# Django functionalities
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

# Local functionalities
from .forms import UserSignupForm, LoginForm, ChangePasswordForm

# ======================================================================================================================
#                                       1. User signup/authorization views
# ======================================================================================================================


def user_signup_view(request):
    """
    Function responsible for rendering the signup template.
    """

    # In case of POST request, create a new User instance
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():

            # Save the new user without committing, and set to it the password
            user = form.save(commit=False)
            cleaned_form = form.cleaned_data
            cleaned_password = cleaned_form['password']
            user.set_password(cleaned_password)

            # Save the new user if the username is unique or render the template for already existing user
            try:
                user.save()
            except IntegrityError:
                return redirect('user_account_exists')

            # Render the template and expose to it the queryset
            return redirect('user_signup_success')

    # In case of GET request, instantiate the form
    else:
        form = UserSignupForm()

    # Render the template and expose to it the queryset
    return render(request, 'users/user_signup.html', {'form': form})


@csrf_exempt
def user_login_view(request):
    """
    Function responsible for rendering the login template.
    """

    # In case of POST request authenticate the User
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            # Authenticate the user with the username and password from the form
            cleaned_form = form.cleaned_data
            cleaned_username = cleaned_form['username']
            cleaned_password = cleaned_form['password']
            user_obj = authenticate(request, username=cleaned_username, password=cleaned_password)

            # Login the user if the authentication was successful, otherwise render the template for invalid login
            if user_obj:
                login(request, user_obj)
                return redirect('vinyl_list')
            else:
                return redirect('user_login_invalid')

    # In case of GET request, instantiate the form
    else:
        form = LoginForm()

    # Render the template and expose to it the queryset
    return render(request, 'users/user_login.html', {'form': form})


def user_logout_view(request):
    """
    Function responsible for rendering the logout template.
    """
    logout(request)
    return render(request, 'users/user_logout_success.html')


def user_change_password_view(request):
    """
    Function responsible for rendering the change password template.
    """

    # In case of POST request, validate the old password and set the new one
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():

            # Check whether the old password is correct
            cleaned_form = form.cleaned_data
            cleaned_password = cleaned_form['password']
            if not request.user.check_password(cleaned_password):
                return redirect('user_invalid_old_password')

            # Set the new password and render the template
            cleaned_new_password = cleaned_form['new_password']
            request.user.set_password(cleaned_new_password)
            request.user.save()
            return redirect('user_password_changed')

    # In case of GET request, instantiate the form
    else:
        form = ChangePasswordForm()

    # Render the template and expose to it the queryset
    return render(request, 'users/user_change_password.html', {'form': form})


# ======================================================================================================================
#                                           1. User retrieve/delete views
# ======================================================================================================================


def user_retrieve_view(request):
    """
    Function responsible for rendering the user details template.
    """
    user_obj = request.user
    return render(request, 'users/user_retrieve.html', {'user_obj': user_obj})


def user_delete_view(request):
    """
    Function responsible for deleting a user profile.
    """
    request.user.delete()
    return redirect('user_delete_success')