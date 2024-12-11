from django.db import models
from django.contrib.auth.models import User
from universe.models import Character


# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Commeny by {self.author} on {self.character.name}"

# Feedback Request Model
class FeedbackRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Feedback request from {self.name}"