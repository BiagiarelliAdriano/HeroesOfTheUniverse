from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


# Create your models here.
class Profile(models.Model):
    """
    Represents a user profile, containing additional information
    about the user, such as their favorite TTRPG and a brief bio.

    Fields:
        - user: A one-to-one relationship with the User model
        - favorite_ttrpg: The user's favorite tabletop RPG. (optional).
        - about_me: A text field for a short bio or description
            of the user (optional).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_ttrpg = models.CharField(max_length=100, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the profile,
        showing the user's username.
        """
        return f"{self.user.username}'s Profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler that creates a Profile instance when a new User is created.

    Args:
        sender: The model class (User).
        instance: The actual instance of the User that was saved.
        created: Boolean flag indicating whether the User instance was created.
        **kwargs: Additional keyword arguments
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal handler that saves the associated Profile instance
    when the User model is saved.

    Args:
        sender: The model class (User).
        instance: The actual instance of the User that was saved.
        **kwargs: Additional keyword arguments.
    """
    instance.profile.save()
