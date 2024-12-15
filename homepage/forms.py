from django import forms
from .models import Comment, FeedbackRequest


class CommentForm(forms.ModelForm):
    """
    A form for creating or updating a comment.
    Only the 'body' field from the Comment model is included in the form.
    """
    class Meta:
        model = Comment
        fields = ['body']


class FeedbackForm(forms.ModelForm):
    """
    A form for submitting feedback, including name, email, and message.
    All fields from the FeedbackRequest model are included in the form.
    """
    class Meta:
        model = FeedbackRequest
        fields = ('name', 'email', 'message')
