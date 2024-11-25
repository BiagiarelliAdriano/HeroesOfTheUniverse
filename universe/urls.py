from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'), # Base URL for the landing page
    path('home/', views.home_page, name='home'), # Home URL
    path('register/', views.register_page, name='register'), # Register URL
]