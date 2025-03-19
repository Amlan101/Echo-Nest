from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm): # This is a form class that inherits from Django's built-in ModelForm class
    class Meta:
        model = Tweet 
        fields = ['text', 'photo'] # These are the fields that will be displayed in the form
