from django import forms
# these are to use built-in django forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# This is to define the user
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # Define fields
        fields = ["username", "email", "password1", "password2"]