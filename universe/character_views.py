from django.shortcuts import render, redirect, get_object_or_404
from .forms import CharacterForm, WeaponFormSet
from .models import Character, Weapon

def create_or_edit_character(request, character_id=None):
    if character_id:
        character = get_object_or_404(Character, id=character_id)
        form = CharacterForm(request.POST or None, instance=character)
        weapon_formset = WeaponFormSet(request.POST or None, queryset=Weapon.objects.filter(character=character))
    else:
        character = Character()
        form = CharacterForm(request.POST or None)
        weapon_formset = WeaponFormSet(request.POST or None)

    if request.method == 'POST' and form.is_valid() and weapon_formset.is_valid():
        character = form.save()
        for weapon_form in weapon_formset:
            weapon = weapon_form.save(commit=False)
            weapon.character = character
            weapon.save
        return redirect('character_detail', character_id=form.instance.id)

    return render(request, 'universe/character.html', {'form': form, 'weapon_formset': weapon_formset})

def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    return render(request, 'character_detail.html', {'character': character})