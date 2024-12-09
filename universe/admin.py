from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models.character_models import Character
from .models import Profile
from homepage.models import Comment

# Register your models here.

# Extend the default UserAdmin to display additional fields
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_favorite_ttrpg')
    def get_favorite_ttrpg(self, obj):
        return obj.profile.favorite_ttrpg
    get_favorite_ttrpg.short_description = 'Favorite TTRPG'
    list_filter = ('is_staff',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Customize the Profile admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite_ttrpg')
    search_fields = ('user__username', 'favorite_ttrpg')
    list_filter = ('favorite_ttrpg',)

admin.site.register(Profile, ProfileAdmin)

# Characters
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'level', 'character_class')
    search_fields = ('name', 'user__username', 'character_class')
    list_filter = ('level', 'character_class')

admin.site.register(Character, CharacterAdmin)

# Comments
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'character', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'character__name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f"{queryset.count()} comments were successfully approved.")

    approve_comments.short_description = "Approve selected comments"

admin.site.register(Comment, CommentAdmin)