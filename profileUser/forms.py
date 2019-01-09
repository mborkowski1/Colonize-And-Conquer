from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from mainPage.models import Profile


class EditEmailForm(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'email'
        }


class EditPasswordForm(UserChangeForm):
    class Meta:
        model = User
        fields = {
            'password'
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {
            'bio',
            'profile_pic'
        }
