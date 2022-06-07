# ======================================================================================================================
#
#                                                  Forms module
#
# ======================================================================================================================

# This is the Forms module of the Users app. These are loaded by the functions in the views.py module.

# ======================================================================================================================
#                                                    Libraries
# ======================================================================================================================

from django import forms
from django.contrib.auth.models import User

# ======================================================================================================================
#                                      1. User signup/authorization forms
# ======================================================================================================================


class UserSignupForm(forms.ModelForm):
    """
    Form for signing up a User.
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean(self):
        """
        Check if the inputted passwords actually match.
        """
        cleaned_data = self.cleaned_data
        if all(key in cleaned_data for key in ('password', 'confirm_password')):
            cleaned_password = cleaned_data['password']
            cleaned_confirm_password = cleaned_data['confirm_password']
            if cleaned_password != cleaned_confirm_password:
                raise forms.ValidationError("Passwords don't match")
        else:
            raise forms.ValidationError("Please fill-in all the required fields")
        return cleaned_data


class LoginForm(forms.Form):
    """
    Form for logging in a User.
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ChangePasswordForm(forms.Form):
    """
    Form for changing the password of a User.
    """
    password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

    def clean(self):
        """
        Check if the inputted passwords actually match.
        """
        cleaned_data = self.cleaned_data
        if all(key in cleaned_data for key in ('new_password', 'confirm_new_password')):
            cleaned_new_password = cleaned_data['new_password']
            cleaned_confirm_new_password = cleaned_data['confirm_new_password']
            if cleaned_new_password != cleaned_confirm_new_password:
                raise forms.ValidationError("Passwords don't match")
        else:
            raise forms.ValidationError("Please fill-in all the required fields")
        return cleaned_data