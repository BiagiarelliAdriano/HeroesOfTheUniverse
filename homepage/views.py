from django.shortcuts import render
from universe.models import Character

# Create your views here.
def home_page(request):
    characters = Character.objects.all().order_by('-id') # Fetch all characters
    return render(request, 'homepage/home.html', {'characters': characters})