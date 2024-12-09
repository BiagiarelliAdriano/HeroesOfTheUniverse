from django.shortcuts import render
from django.contrib import messages
from .models import Comment
from .forms import CommentForm
from universe.models import Character

def home_page(request):
    characters = Character.objects.all().order_by('-id')  # Fetch all characters
    comment_form = CommentForm()

    for character in characters:
        character.approved_comments = character.comments.filter(approved=True)

    if request.method == 'POST':
        # Handle comment submission
        character_id = request.POST.get('character_id')
        comment_body = request.POST.get('body')

        if character_id and comment_body:
            # Get the character object
            character = Character.objects.get(id=character_id)

            # Create a new comment
            comment = Comment.objects.create(
                author=request.user,
                body=comment_body,
                character=character,
                approved=False
            )

            messages.success(request, "Your comment has been submitted and is awaiting approval.")

    return render(
        request,
        'homepage/home.html',
        {'characters': characters, 'comment_form': comment_form},
    )
