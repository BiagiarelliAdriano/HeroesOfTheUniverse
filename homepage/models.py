from django.db import models
from django.contrib.auth.models import User
from universe.models import Character


# Create your models here.
class Comment(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)