from django.db import models
from .character_models import Character

class Spell(models.Model):
    # Spell details
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="spells")
    level = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    casting_time = models.CharField(max_length=100)
    spell_range = models.CharField(max_length=100)

    # Spell Attributes
    concentration = models.BooleanField(default=False)
    ritual = models.BooleanField(default=False)
    material_required = models.BooleanField(default=False)

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (Level {self.level})"