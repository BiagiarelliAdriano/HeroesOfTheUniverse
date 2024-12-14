from django.urls import path, include
from . import views, character_views

app_name = 'universe'
urlpatterns = [
    path('', views.landing_page, name='landing'), # Base URL for the landing page
    path('register/', views.register_or_login, name='register_or_login'), # Register/Login URL
    path('profile/<str:username>/', views.profile_view, name='profile'), # Profile URL
    path('character/', character_views.create_or_edit_character, name='make_character'), # Make A Character URL
    path('character/<int:pk>/', character_views.character_detail, name='character_detail'), # Character Details After Creation URL
    path('logout/', views.logout_view_page, name='logout'), # Logout URL
    path('character/delete/<int:character_id>/', views.delete_character, name='delete_character'), # Character Deletion URL
]