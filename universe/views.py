from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms

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
    favorite_ttrpg = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [('username', 'password')]

def register_or_login(request):
    if request.user.is_authenticated: # User is already logged in
        return redirect('home')

    if request.method == 'POST':
        if 'register' in request.POST: # User submitted the registration form
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.set_password(register_form.cleaned_data['password']) # Hash password
                user.save()
                messages.success(request, "Account created successfully! You can now log in.")
                return redirect('/register') # Redirect to login form
        elif 'login' in request.POST: # User submitted the login form
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/home')
                else:
                    messages.error(request, "Invalid credentials, please try again.")
    else: # If no form was submitted
        register_form = RegisterForm()
        login_form = AuthenticationForm()

    return render(request, 'register.html', {
        'register_form': register_form,
        'login_form': login_form,
    })