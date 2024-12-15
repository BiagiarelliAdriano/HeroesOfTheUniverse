from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django import forms
from .models import Profile, Character


def landing_page(request):
    """
    Renders the landing page template. If the user is authenticated,
    they are redirected to the main home page instead.
    """
    if request.user.is_authenticated:
        return redirect('main_home:home')

    return render(request, 'universe/landing.html')


def home_page(request):
    """
    Renders the home page template.
    """
    return render(request, 'homepage/home.html')


def register_page(request):
    """
    Renders the register/login page template.
    """
    return render(request, 'universe/register.html')


def profile_page(request):
    """
    Renders the profile page template for the authenticated user.

    If the user is not authenticated, they are redirected to the registration page.
    """
    if not request.user.is_authenticated:
        return redirect('universe:register_or_login')

    return render(request, 'universe/profile.html')


def logout_view_page(request):
    """
    Logs the user out and redirects to the home page.
    """
    logout(request)
    return redirect('main_home:home')


class RegisterForm(forms.ModelForm):
    """
    Custom registration form for user registration,
    including a password and favorite TTRPG field.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    favorite_ttrpg = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'password']


def register_or_login(request):
    """
    Handles user registration and login. If no 'login' key is in the POST data,
    the function registers the user; otherwise, it attempts to log the user in.
    """
    if request.method == 'POST':
        if 'login' not in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            favorite_ttrpg = request.POST.get('favorite_ttrpg')

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return render(request, 'universe/register.html')

            try:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.profile.favorite_ttrpg = favorite_ttrpg
                user.profile.save()
            except Exception as e:
                messages.error(request, f"Error creating user: {str(e)}")
                return render(request, 'universe/register.html')

            login(request, user)
            return redirect('main_home:home')

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


def profile_view(request, username):
    """
    Displays and allows editing of a user's profile.
    Only the user who owns the profile can edit it.
    """
    if not request.user.is_authenticated and username == 'guest':
        return redirect('universe:register_or_login')

    user_profile = get_object_or_404(Profile, user__username=username)
    is_owner = request.user == user_profile.user

    if request.method == "POST" and is_owner:
        if "username" in request.POST:
            new_username = request.POST.get("username").strip()
            if not new_username or len(new_username) > 50:
                messages.error(
                        request,
                        "Username cannot be empty or longer than 50 letters.")
            elif User.objects.filter(username=new_username).exists():
                messages.error(request, "This username is already taken.")
            else:
                request.user.username = new_username
                request.user.save()

        if "favorite_ttrpg" in request.POST:
            favorite_ttrpg = request.POST.get("favorite_ttrpg")
            if len(favorite_ttrpg) > 50:
                messages.error(
                    request,
                    "Favorite TTRPG cannot be longer than 50 letters.")
            else:
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
    """
    Deletes a character. The user can only delete characters they own.
    """
    if not request.user.is_authenticated:
        return redirect('universe:register_or_login')

    character = get_object_or_404(Character, id=character_id)

    if character.user != request.user:
        messages.error(
            request, "You are not authorized to delete this character.")
        return redirect('universe:profile', username=request.user.username)

    character.delete()
    messages.success(
        request,
        f"Character '{character.name}' "
        "was successfully sent to the Nine Hells!")

    return redirect('universe:profile', username=request.user.username)
