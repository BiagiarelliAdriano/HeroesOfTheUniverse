from django.shortcuts import render, redirect, get_object_or_404
from .forms import CharacterForm
from .models import Character

def create_or_edit_character(request, character_id=None):
    if character_id:
        character = get_object_or_404(Character, id=character_id)
        form = CharacterForm(request.POST or None, instance=character)
    else:
        character = Character()
        form = CharacterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('character_detail', character_id=form.instance.id)

    return render(request, 'universe/character.html', {'form': form})

def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    return render(request, 'character_detail.html', {'character': character})