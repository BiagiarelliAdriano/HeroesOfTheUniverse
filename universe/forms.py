from django import forms
from django.forms import modelformset_factory
from .models import Character, Weapon

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name', 'background', 'species', 'character_class', 'subclass',
            'level', 'xp', 'class_image', 'armor_class', 'shield', 'current_hit_points',
            'temp_hit_points', 'max_hit_points', 'spent_hit_dice', 'max_hit_dice',
            'death_save_success', 'death_save_failures', 'initiative', 'speed', 'size',
            'passive_perception', 'proficiency_bonus', 'strength_score', 'strength_modifier',
            'dexterity_score', 'dexterity_modifier', 'constitution_score', 'constitution_modifier',
            'intelligence_score', 'intelligence_modifier', 'wisdom_score', 'wisdom_modifier',
            'charisma_score', 'charisma_modifier', 'strength_saving_throw', 'dexterity_saving_throw',
            'constitution_saving_throw', 'intelligence_saving_throw', 'wisdom_saving_throw', 'charisma_saving_throw',
            'athletic_skill', 'acrobatics_skill', 'sleight_of_hand_skill', 'stealth_skill',
            'arcana_skill', 'history_skill', 'investigation_skill', 'nature_skill', 'religion_skill',
            'animal_handling_skill', 'insight_skill', 'medicine_skill', 'perception_skill', 'survival_skill',
            'deception_skill', 'intimidation_skill', 'performance_skill', 'persuasion_skill',
            'class_features_1', 'class_features_2', 'heroic_inspiration', 'light_armor_training', 'medium_armor_training',
            'heavy_armor_training', 'shield_armor_training', 'weapons_proficiencies', 'tools_proficiencies',
            'species_traits', 'feats',
        ]
    
    class_image = forms.ChoiceField(choices=Character.CLASS_IMAGE_CHOICES, widget=forms.RadioSelect, required=False)

class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ['name', 'attack_bonus_save_dc', 'damage_type', 'weapon_notes']

WeaponFormSet = modelformset_factory(Weapon, form=WeaponForm, extra=3)