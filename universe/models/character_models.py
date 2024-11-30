from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    # Basic Character Info
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    background = models.CharField(max_length=100, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    character_class = models.CharField(max_length=100, blank=True, null=True)
    subclass = models.CharField(max_length=100, blank=True, null=True)
    level = models.PositiveIntegerField(default=1)
    xp = models.PositiveIntegerField(default=1)

    # Combat Stats
    armor_class = models.PositiveIntegerField(default=10)
    shield = models.BooleanField(default=False)
    current_hit_points = models.PositiveIntegerField(default=0)
    temp_hit_points = models.PositiveIntegerField(default=0)
    max_hit_points = models.PositiveIntegerField(default=0)
    spent_hit_dice = models.PositiveIntegerField(default=0)
    max_hit_dice = models.PositiveIntegerField(default=0)

    # Death Saves
    death_save_success = models.PositiveIntegerField(default=0)
    death_save_failures = models.PositiveIntegerField(default=0)

    # Other Combat Stats
    initiative = models.IntegerField(default=0)
    speed = models.PositiveIntegerField(default=30)
    size = models.CharField(max_length=100, blank=True, null=True)
    passive_perception = models.PositiveIntegerField(default=10)
    proficiency_bonus = models.IntegerField(default=2)

    # Ability Scores And Modifiers
    strength_score = models.PositiveIntegerField(default=10)
    strength_modifier = models.IntegerField(default=0)
    dexterity_score = models.PositiveIntegerField(default=10)
    dexterity_modifier = models.IntegerField(default=0)
    constitution_score = models.PositiveIntegerField(default=10)
    constitution_modifier = models.IntegerField(default=0)
    intelligence_score = models.PositiveIntegerField(default=10)
    intelligence_modifier = models.IntegerField(default=0)
    wisdom_score = models.PositiveIntegerField(default=10)
    wisdom_modifier = models.IntegerField(default=0)
    charisma_score = models.PositiveIntegerField(default=10)
    charisma_modifier = models.IntegerField(default=0)

    # Saving Throws
    strength_saving_throw = models.BooleanField(default=False)
    dexterity_saving_throw = models.BooleanField(default=False)
    constitution_saving_throw = models.BooleanField(default=False)
    intelligence_saving_throw = models.BooleanField(default=False)
    wisdom_saving_throw = models.BooleanField(default=False)
    charisma_saving_throw = models.BooleanField(default=False)

    # Skills
    athletic_skill = models.BooleanField(default=False)
    acrobatics_skill = models.BooleanField(default=False)
    sleight_of_hand_skill = models.BooleanField(default=False)
    stealth_skill = models.BooleanField(default=False)
    arcana_skill = models.BooleanField(default=False)
    history_skill = models.BooleanField(default=False)
    investigation_skill = models.BooleanField(default=False)
    nature_skill = models.BooleanField(default=False)
    religion_skill = models.BooleanField(default=False)
    animal_handling_skill = models.BooleanField(default=False)
    insight_skill = models.BooleanField(default=False)
    medicine_skill = models.BooleanField(default=False)
    perception_skill = models.BooleanField(default=False)
    survival_skill = models.BooleanField(default=False)
    deception_skill = models.BooleanField(default=False)
    intimidation_skill = models.BooleanField(default=False)
    performance_skill = models.BooleanField(default=False)
    persuasion_skill = models.BooleanField(default=False)

    # Features And Proficiencies
    class_features_1 = models.TextField(blank=True, null=True)
    class_features_2 = models.TextField(blank=True, null=True)
    heroic_inspiration = models.BooleanField(default=False)
    light_armor_training = models.BooleanField(default=False)
    medium_armor_training = models.BooleanField(default=False)
    heavy_armor_training = models.BooleanField(default=False)
    shield_armor_training = models.BooleanField(default=False)
    weapons_proficiencies = models.TextField(blank=True, null=True)
    tools_proficiencies = models.TextField(blank=True, null=True)
    species_traits = models.TextField(blank=True, null=True)
    feats = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

    def save(self, *args, **kwargs):
        if not Character.objects.filter(name=self.name).exists():
            super().save(*args, **kwargs)