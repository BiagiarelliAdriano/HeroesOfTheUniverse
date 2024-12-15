from django.urls import path
from . import views

"""
URL configuration for the 'homepage' app.

This module defines the URL patterns for the homepage, including:
- The home page view (`home_page`).
- The feedback submission page (`feedback_page`).

These URL patterns are included in the main URL configuration of the project.
"""

app_name = 'main_home'
urlpatterns = [
    path('', views.home_page, name='home'),  # Home URL
    path('feedback/', views.feedback_page, name='feedback')  # Feedback URL
]
