from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CharacterForm, WeaponFormSet, SpellFormSet
from .models import Character, Weapon

def create_or_edit_character(request, character_id=None):
    if not request.user.is_authenticated:
        return redirect('universe:register_or_login')

    if character_id:
        character = get_object_or_404(Character, id=character_id)
        form = CharacterForm(request.POST or None, instance=character)
        weapon_formset = WeaponFormSet(request.POST or None, queryset=Weapon.objects.filter(character=character))
        spell_formset = SpellFormSet(request.POST or None, queryset=character.spells.all())
    else:
        form = CharacterForm(request.POST or None)
        weapon_formset = WeaponFormSet(request.POST or None)
        spell_formset = SpellFormSet(request.POST or None)

    if request.method == 'POST':
        if form.is_valid() and weapon_formset.is_valid() and spell_formset.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()

            weapons = weapon_formset.save(commit=False)
            for weapon in weapons:
                weapon.character = character
                weapon.save()

            spells = spell_formset.save(commit=False)
            for spell in spells:
                spell.character = character
                spell.save()

            messages.success(request, 'Character successfully created! Good job!')
            return redirect('character_detail', pk=character.id)

    return render(request, 'universe/character.html', {'form': form, 'weapon_formset': weapon_formset, 'spell_formset': spell_formset,})

def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    form = CharacterForm(instance=character)
    weapon_formset = WeaponFormSet(request.POST or None, queryset=Weapon.objects.filter(character=character))
    spell_formset = SpellFormSet(request.POST or None, queryset=character.spells.all())

    if request.user.username != character.user.username:
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True

    return render(
        request,
        'universe/character_detail.html',
        {
            'form': form,
            'character': character,
            'weapon_formset': weapon_formset,
            'spell_formset': spell_formset,
        }
    )