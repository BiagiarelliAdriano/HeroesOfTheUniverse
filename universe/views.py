from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from .models import Profile

# Create your views here.
def landing_page(request):
    if request.user.is_authenticated: # If user is logged in
        return redirect('home') # Redirect to the Home page
    
    return render(request, 'universe/landing.html') # Render the landing page template

def home_page(request):
    return render(request, 'universe/home.html') # Render the Home page template

def register_page(request):
    return render(request, 'universe/register.html') # Render the Register/Log In page template

def profile_page(request):
    return render(request, 'universe/profile.html') # Render the Profile page template

def make_character_page(request):
    return render(request, 'universe/character.html') # Render the Make A Character template

def logout_view_page(request):
    logout(request)
    return redirect('home') # Render the logout function and returns to home template

# Custom Registration Form
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    favorite_ttrpg = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'password']

def register_or_login(request):
    if request.method == 'POST':
        # Process Registration Form
        username = request.POST.get('username')
        password = request.POST.get('password')
        favorite_ttrpg = request.POST.get('favorite_ttrpg')

        # Check if the user exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another.")
            return redirect('/register') # Redirect back to registration page

        # Create user
        user = User.objects.create_user(username=username, password=password)

        # Log in user
        login(request, user)

        # Redirect to home page
        return redirect('/home')
    
    # Default behavior: render the page
    return render(request, 'universe/register.html')