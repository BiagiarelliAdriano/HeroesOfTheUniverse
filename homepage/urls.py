from django.urls import path
from . import views

app_name = 'main_home'
urlpatterns = [
    path('', views.home_page, name='home'), # Home URL
    path('feedback/', views.feedback_page, name='feedback'), # Feedback URL
]