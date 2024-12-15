from django.urls import path, include
from . import views, character_views

"""
URL configuration for the 'universe' app.

This module defines the URL patterns for various views in the universe app:
- Landing page.
- Registration/login page.
- User profile page.
- Character creation, details, and deletion pages.
- Logout page.
"""

app_name = 'universe'
urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('register/', views.register_or_login, name='register_or_login'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('character/', character_views.create_or_edit_character,
         name='make_character'),
    path('character/<int:pk>/', character_views.character_detail,
         name='character_detail'),
    path('logout/', views.logout_view_page, name='logout'),
    path('character/delete/<int:character_id>/', views.delete_character,
         name='delete_character'),
]
