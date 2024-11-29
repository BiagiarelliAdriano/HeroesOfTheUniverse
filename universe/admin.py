from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models.character_models import Character
from .models import Profile

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
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'character_class')
    search_fields = ('name', 'character_class')