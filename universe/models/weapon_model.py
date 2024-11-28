from django.db import models
from .character_models import Character

class Weapon(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='weapons')
    name = models.CharField(max_length=100)
    attack_bonus_save_dc = models.IntegerField(default=0)
    damage_type = models.CharField(max_length=100)
    weapon_notes = models.CharField(max_length=100)

    def __str__(self):
        return self.name