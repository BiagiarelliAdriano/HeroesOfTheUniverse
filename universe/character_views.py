from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CharacterForm
from .models import Character


def create_or_edit_character(request, character_id=None):
    if not request.user.is_authenticated:
        return redirect('universe:register_or_login')

    if character_id:
        character = get_object_or_404(Character, id=character_id)
        form = CharacterForm(request.POST or None, instance=character)
    else:
        form = CharacterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()

            messages.success(request,
                             'Character successfully created! Good job!')
            return redirect('universe:character_detail', pk=character.id)

    return render(request, 'universe/character.html', {
        'form': form,
        'character': character if character_id else None,
    })


def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)

    # Check if the logged-in user is the character owner
    if request.user.username != character.user.username:
        form = CharacterForm(instance=character)  # Read-only view
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
        if request.method == "POST":
            messages.error(request, "You cannot edit this character because you do not own it.")
    else:
        form = CharacterForm(request.POST or None, instance=character)  # Editable form

        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, 'Character successfully edited!')
                return redirect('universe:character_detail', pk=character.pk)

    return render(
        request,
        'universe/character_detail.html',
        {
            'form': form,
            'character': character,
        }
    )
