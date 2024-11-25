from django.shortcuts import render, redirect

# Create your views here.
def landing_page(request):
    if request.user.is_authenticated: # If user is logged in
        return redirect('home') # Redirect to the Home page
    
    return render(request, 'universe/landing.html') # Render the landing page template

def home_page(request):
    return render(request, 'universe/home.html') # Render the Home page template

def register_page(request):
    return render(request, 'universe/register.html') # Render the Register/Log In page template