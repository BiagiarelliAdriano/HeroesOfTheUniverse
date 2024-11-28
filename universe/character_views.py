from django.shortcuts import render, redirect
from .forms import CharacterForm
from .models import Character

def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            # Save the character (this creates a new character)
            character = form.save(commit=False)
            character.user = request.user # Associate the character with the logged-in user
            character.save()
            return redirect('character_detail', character_id=character.id)
    else:
        form = CharacterForm()

    return render(request, 'character.html', {'form': form})