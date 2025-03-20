from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm): # This is a form class that inherits from Django's built-in ModelForm class
    class Meta:
        model = Tweet 
        fields = ['text', 'photo'] # These are the fields that will be displayed in the form

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    