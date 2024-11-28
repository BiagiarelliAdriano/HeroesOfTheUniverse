from django.urls import path
from . import views, character_views

urlpatterns = [
    path('', views.landing_page, name='landing'), # Base URL for the landing page
    path('home/', views.home_page, name='home'), # Home URL
    path('register/', views.register_or_login, name='register_or_login'),
    path('profile/', views.profile_page, name='profile'), # Profile URL
    path('character/', character_views.create_or_edit_character, name='make_character'), # Make A Character URL
    path('logout/', views.logout_view_page, name='logout'), # Logout URL
]