from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CharacterForm, WeaponFormSet
from .models import Character, Weapon

def create_or_edit_character(request, character_id=None):
    if character_id:
        character = get_object_or_404(Character, id=character_id)
        form = CharacterForm(request.POST or None, instance=character)
        weapon_formset = WeaponFormSet(request.POST or None, queryset=Weapon.objects.filter(character=character))
    else:
        form = CharacterForm(request.POST or None)
        weapon_formset = WeaponFormSet(request.POST or None)

    if request.method == 'POST':
        if form.is_valid() and weapon_formset.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()

            weapons = weapon_formset.save(commit=False)
            for weapon in weapons:
                weapon.character = character
                weapon.save()

            messages.success(request, 'Character successfully created! Good job!')
            return redirect('character_detail', character_id=character.id)

    return render(request, 'universe/character.html', {'form': form, 'weapon_formset': weapon_formset})