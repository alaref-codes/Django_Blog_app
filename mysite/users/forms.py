from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Required argument default to True

    class Meta: # The Meta class k eep the configuration in one place
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
