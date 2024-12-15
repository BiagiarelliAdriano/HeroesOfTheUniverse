from django.contrib import admin
from django.contrib.admin import TabularInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models.character_models import Character
from .models import Profile
from homepage.models import Comment, FeedbackRequest

# Register your models here.


# Extend the default UserAdmin to display additional fields
class CustomUserAdmin(UserAdmin):
    """
    Custom User admin class to display the user's favorite TTRPG
    alongside standard fields in the Django admin panel.

    Attributes:
        list_display: The fields to display in the user list view.
        get_favorite_ttrpg: Custom method to display the user's favorite TTRPG.
        list_filter: Fields to filter the list of users by.
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff',
                    'get_favorite_ttrpg')

    def get_favorite_ttrpg(self, obj):
        """
        Returns the favorite tabletop RPG of the user from their profile.

        Args:
            obj: The user object.
        """
        return obj.profile.favorite_ttrpg
    get_favorite_ttrpg.short_description = 'Favorite TTRPG'
    list_filter = ('is_staff',)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# Customize the Profile admin
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for the Profile model, allowing search and filtering
    by user and favorite TTRPG.

    Attributes:
        list_display: The fields to display in the profile list view.
        search_fields: Fields that can be searched in the admin panel.
        list_filter: Fields to filter the list of profiles by.
    """
    list_display = ('user', 'favorite_ttrpg')
    search_fields = ('user__username', 'favorite_ttrpg')
    list_filter = ('favorite_ttrpg',)


admin.site.register(Profile, ProfileAdmin)


# Characters
class CharacterAdmin(admin.ModelAdmin):
    """
    Admin interface for the Character model, allowing search and filtering
    by character name, class, and level.

    Attributes:
        list_display: The fields to display in the character list view.
        search_fields: Fields that can be searched in the admin panel.
        list_filter: Fields to filter the list of characters by.
    """
    list_display = ('name', 'user', 'level', 'character_class')
    search_fields = ('name', 'user__username', 'character_class')
    list_filter = ('level', 'character_class')


admin.site.register(Character, CharacterAdmin)


# Comments
class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface for the Comment model, allowing search, filtering,
    and actions like approving comments.

    Attributes:
        list_display: The fields to display in the comment list view.
        list_filter: Fields to filter the list of comments by.
        search_fields: Fields that can be searched in the admin panel.
        actions: List of actions to be performed on selected comments.
    """
    list_display = ('author', 'character', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'character__name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Custom action to approve selected comments.

        Args:
            request: The current request.
            queryset: The selected comments to approve.
        """
        queryset.update(approved=True)
        self.message_user(
            request,
            f"{queryset.count()} comments were successfully approved.")

    approve_comments.short_description = "Approve selected comments"


admin.site.register(Comment, CommentAdmin)


# Feedback Request Admin
@admin.register(FeedbackRequest)
class FeedbackRequestAdmin(admin.ModelAdmin):
    """
    Admin interface for the FeedbackRequest model, allowing display of
    feedback message and read status.

    Attributes:
    list_display: The fields to display in the feedback request list view.
    """
    list_display = ('message', 'read',)
