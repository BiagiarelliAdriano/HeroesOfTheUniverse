from django.db import models
from django.contrib.auth.models import User
from universe.models import Character


# Create your models here.
class Comment(models.Model):
    """
    Represents a comment made by a user on a character's post.

    Fields:
        author: The user who wrote the comment (ForeignKey to User).
        character: The character the comment is about
        (ForeignKey to Character).
        body: The content of the comment.
        created_on: The date and time when the comment was created.
        approved: A boolean indicating if the comment has been approved.

    Methods:
        __str__: Returns a string representation of the comment,
        showing the author and the character's name.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE,
                                  related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.author} on {self.character.name}"


# Feedback Request Model
class FeedbackRequest(models.Model):
    """
    Represents a feedback request submitted by a user.

    Fields:
        name: The name of the person submitting the feedback.
        email: The email address of the person submitting the feedback.
        message: The content of the feedback message.
        read: A boolean indicating if the feedback has been read.

    Methods:
        __str__: Returns a string representation of the feedback request,
        showing the submitter's name.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Feedback request from {self.name}"
