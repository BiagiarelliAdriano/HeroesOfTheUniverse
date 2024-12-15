from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CharacterForm
from .models import Character


def create_or_edit_character(request, character_id=None):
    """
    Handles the creation or editing of a character.
    If a character_id is provided, the function allows editing of the
    corresponding character, otherwise, it creates a new character.

    If the request is not authenticated, the user is redirected to the
    login page. After successful submission, the user is redirected to the
    character detail page.

    Args:
        request: The HTTP request object.
        character_id: Optional ID of the character to edit (default is None).

    Returns:
        A rendered character creation/edit page or a redirect to the character
        detail page after saving.
    """
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
    """
    Displays the details of a specific character. If the logged-in user is the
    owner of the character, they are allowed to edit it. Otherwise,
    the character is displayed in a read-only mode.

    Args:
        request: The HTTP request object.
        pk: The primary key (ID) of the character to view.

    Returns:
        A rendered character detail page, which either allows editing or
        shows a read-only view.
    """
    character = get_object_or_404(Character, pk=pk)

    # Check if the logged-in user is the character owner
    if request.user.username != character.user.username:
        form = CharacterForm(instance=character)  # Read-only view
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
        if request.method == "POST":
            messages.error(
                request,
                "You cannot edit this character because you do not own it.")
    else:
        # Editable form
        form = CharacterForm(request.POST or None, instance=character)

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
