from django import forms
from .models import Comment, FeedbackRequest

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackRequest
        fields = ('name', 'email', 'message')