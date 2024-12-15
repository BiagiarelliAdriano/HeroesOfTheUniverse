from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django import forms
from .models import Profile, Character

# Create your views here.
def landing_page(request):
    if request.user.is_authenticated: # If user is logged in
        return redirect('main_home:home') # Redirect to the Home page
    
    return render(request, 'universe/landing.html') # Render the landing page template

def home_page(request):
    return render(request, 'homepage/home.html') # Render the Home page template

def register_page(request):
    return render(request, 'universe/register.html') # Render the Register/Log In page template

def profile_page(request):
    if not request.user.is_authenticated:
        return redirect('universe:register_or_login')

    return render(request, 'universe/profile.html') # Render the Profile page template

def logout_view_page(request):
    logout(request)
    return redirect('main_home:home') # Render the logout function and returns to home template

# Custom Registration Form
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    favorite_ttrpg = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'password']

def register_or_login(request):
    if request.method == 'POST':
        # Registration logic (if no 'login' key is present in POST)
        if 'login' not in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            favorite_ttrpg = request.POST.get('favorite_ttrpg')

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return render(request, 'universe/register.html')

            # Create the user
            try:
                user = User.objects.create_user(username=username, password=password)
                user.profile.favorite_ttrpg = favorite_ttrpg
                user.profile.save()
            except Exception as e:
                messages.error(request, f"Error creating user: {str(e)}")
                return render(request, 'universe/register.html')

            # Log the user in
            login(request, user)
            return redirect('main_home:home')

        # Login logic (if 'login' key is present in POST)
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_home:home')
            else:
                messages.error(request, "Invalid username or password.")
                return render(request, 'universe/register.html')

    return render(request, 'universe/register.html')

# Profile Page Functionality
def profile_view(request, username):
    # Redirect unauthenticated users to the registration page
    if not request.user.is_authenticated and username == 'guest':
        return redirect('universe:register_or_login')

    # Fetch the profile based on the username
    user_profile = get_object_or_404(Profile, user__username=username)
    is_owner = request.user == user_profile.user

    if request.method == "POST" and is_owner:
        # Update profile logic if the user is the owner
        if "favorite_ttrpg" in request.POST:
            favorite_ttrpg = request.POST.get("favorite_ttrpg")
            user_profile.favorite_ttrpg = favorite_ttrpg

        if "about_me" in request.POST:
            about_me = request.POST.get("about_me")
            user_profile.about_me = about_me

        user_profile.save()
        messages.success(request, "Profile edited successfully!")

    context = {
        "user_profile": user_profile,
        "is_owner": is_owner,
    }
    return render(request, "universe/profile.html", context)

def delete_character(request, character_id):
    if not request.user.is_authenticated:
        return redirect('universe:register_or_login')

    character = get_object_or_404(Character, id=character_id)

    if character.user != request.user:
        messages.error(request, "You are not authorized to delete this character.")
        return redirect('universe:profile', username=request.user.username)

    character.delete()
    messages.success(request, f"Character '{character.name}' was successfully sent to the Nine Hells!")

    return redirect('universe:profile', username=request.user.username)