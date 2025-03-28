from django.db import models
from django.contrib.auth.models import User # Django's built-in user model which is present in the admin page when you run the server   

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE deletes the tweet if the user is deleted
    text = models.TextField(max_length=500) 
    photo = models.ImageField(upload_to='tweet_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} tweeted: {self.text}'

