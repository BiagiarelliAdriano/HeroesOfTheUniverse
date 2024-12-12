from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    # Basic Character Info
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User's name
    name = models.CharField(max_length=100, unique=True) # Character's name
    background = models.CharField(max_length=100, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    character_class = models.CharField(max_length=100, blank=True, null=True)
    subclass = models.CharField(max_length=100, blank=True, null=True)
    level = models.PositiveIntegerField(default=1)
    xp = models.PositiveIntegerField(default=1)  # Experience Points

    # Class Image
    CLASS_IMAGE_CHOICES = [
        ('barbarian', 'Barbarian'),
        ('bard', 'Bard'),
        ('cleric', 'Cleric'),
        ('druid', 'Druid'),
        ('fighter', 'Fighter'),
        ('monk', 'Monk'),
        ('paladin', 'Paladin'),
        ('ranger', 'Ranger'),
        ('rogue', 'Rogue'),
        ('sorcerer', 'Sorcerer'),
        ('warlock', 'Warlock'),
        ('wizard', 'Wizard'),
    ]

    class_image = models.CharField(
        max_length=50,
        choices=CLASS_IMAGE_CHOICES,
        default='barbarian',
        blank=True,
        null=True
    )

    # Combat Stats
    armor_class = models.PositiveIntegerField(default=10)
    shield = models.BooleanField(default=False)
    current_hit_points = models.PositiveIntegerField(default=0)
    temp_hit_points = models.PositiveIntegerField(default=0) # Temporary Hit Points
    max_hit_points = models.PositiveIntegerField(default=0) # Maximum Hit Points
    spent_hit_dice = models.PositiveIntegerField(default=0)
    max_hit_dice = models.PositiveIntegerField(default=0) # Maximum Hit Dice

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

    # 2nd Page Content - Spellcasting
    spellcasting_ability = models.CharField(max_length=100, blank=True, null=True)
    spellcasting_modifier = models.IntegerField(default=0)
    spell_save_dc = models.IntegerField(default=0) # Spell Saving Throw Difficulty Class
    spell_attack_bonus = models.IntegerField(default=0)

    # Spell Slots
    spell_slots_total_level_1 = models.IntegerField(default=0)
    spell_slots_used_level_1_1 = models.BooleanField(default=False)
    spell_slots_used_level_1_2 = models.BooleanField(default=False)
    spell_slots_used_level_1_3 = models.BooleanField(default=False)
    spell_slots_used_level_1_4 = models.BooleanField(default=False)

    spell_slots_total_level_2 = models.IntegerField(default=0)
    spell_slots_used_level_2_1 = models.BooleanField(default=False)
    spell_slots_used_level_2_2 = models.BooleanField(default=False)
    spell_slots_used_level_2_3 = models.BooleanField(default=False)

    spell_slots_total_level_3 = models.IntegerField(default=0)
    spell_slots_used_level_3_1 = models.BooleanField(default=False)
    spell_slots_used_level_3_2 = models.BooleanField(default=False)
    spell_slots_used_level_3_3 = models.BooleanField(default=False)

    spell_slots_total_level_4 = models.IntegerField(default=0)
    spell_slots_used_level_4_1 = models.BooleanField(default=False)
    spell_slots_used_level_4_2 = models.BooleanField(default=False)
    spell_slots_used_level_4_3 = models.BooleanField(default=False)

    spell_slots_total_level_5 = models.IntegerField(default=0)
    spell_slots_used_level_5_1 = models.BooleanField(default=False)
    spell_slots_used_level_5_2 = models.BooleanField(default=False)
    spell_slots_used_level_5_3 = models.BooleanField(default=False)

    spell_slots_total_level_6 = models.IntegerField(default=0)
    spell_slots_used_level_6_1 = models.BooleanField(default=False)
    spell_slots_used_level_6_2 = models.BooleanField(default=False)

    spell_slots_total_level_7 = models.IntegerField(default=0)
    spell_slots_used_level_7_1 = models.BooleanField(default=False)
    spell_slots_used_level_7_2 = models.BooleanField(default=False)

    spell_slots_total_level_8 = models.IntegerField(default=0)
    spell_slots_used_level_8_1 = models.BooleanField(default=False)

    spell_slots_total_level_9 = models.IntegerField(default=0)
    spell_slots_used_level_9_1 = models.BooleanField(default=False)

    # Additional Fields
    appearance_area = models.TextField(blank=True, null=True)
    backstory_personality = models.TextField(blank=True, null=True)
    alignment = models.CharField(max_length=100, blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    equipment = models.TextField(blank=True, null=True)

    # Magic Attunements
    magic_attunement_1 = models.BooleanField(default=False)
    magic_attunement_1_name = models.CharField(max_length=100, blank=True, null=True)

    magic_attunement_2 = models.BooleanField(default=False)
    magic_attunement_2_name = models.CharField(max_length=100, blank=True, null=True)

    magic_attunement_3 = models.BooleanField(default=False)
    magic_attunement_3_name = models.CharField(max_length=100, blank=True, null=True)

    # Currency
    cp = models.PositiveIntegerField(default=0)  # Copper Pieces
    sp = models.PositiveIntegerField(default=0)  # Silver Pieces
    ep = models.PositiveIntegerField(default=0)  # Electrum Pieces
    gp = models.PositiveIntegerField(default=0)  # Gold Pieces
    pp = models.PositiveIntegerField(default=0)  # Platinum Pieces

    def __str__(self):
        return f"{self.name} ({self.user.username})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)