from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Required argument defaul to True

    class Meta: # The Meta class keep the configuration in one place
        model = User
        fields = ['username','email','password1','password2']
