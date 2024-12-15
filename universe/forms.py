from django import forms
from .models import Character

"""
Form for the 'universe' app, specifically for character creation and editing.

This file contains the CharacterForm, which is a ModelForm for the
Character model. It handles the input and validation for various fields
associated with character attributes, abilities, skills, equipment, spells,
and other RPG-related details.

The form includes a custom field for class image selection,
with choices defined in the Character model.
"""


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name', 'background', 'species', 'character_class', 'subclass',
            'level', 'xp', 'class_image', 'armor_class', 'shield',
            'current_hit_points', 'temp_hit_points', 'max_hit_points',
            'spent_hit_dice', 'max_hit_dice', 'death_save_success',
            'death_save_failures', 'initiative', 'speed', 'size',
            'passive_perception', 'proficiency_bonus', 'strength_score',
            'strength_modifier', 'dexterity_score', 'dexterity_modifier',
            'constitution_score', 'constitution_modifier',
            'intelligence_score', 'intelligence_modifier', 'wisdom_score',
            'wisdom_modifier', 'charisma_score', 'charisma_modifier',
            'strength_saving_throw', 'dexterity_saving_throw',
            'constitution_saving_throw', 'intelligence_saving_throw',
            'wisdom_saving_throw', 'charisma_saving_throw', 'athletic_skill',
            'acrobatics_skill', 'sleight_of_hand_skill', 'stealth_skill',
            'arcana_skill', 'history_skill', 'investigation_skill',
            'nature_skill', 'religion_skill', 'animal_handling_skill',
            'insight_skill', 'medicine_skill', 'perception_skill',
            'survival_skill', 'deception_skill', 'intimidation_skill',
            'performance_skill', 'persuasion_skill', 'class_features_1',
            'class_features_2', 'heroic_inspiration', 'light_armor_training',
            'medium_armor_training', 'heavy_armor_training',
            'shield_armor_training', 'weapons_proficiencies',
            'tools_proficiencies', 'species_traits', 'feats',
            'weapon_name_1', 'attack_bonus_save_dc_1', 'damage_type_1',
            'weapon_notes_1', 'weapon_name_2', 'attack_bonus_save_dc_2',
            'damage_type_2', 'weapon_notes_2',
            'spellcasting_ability', 'spellcasting_modifier', 'spell_save_dc',
            'spell_attack_bonus', 'spell_slots_used_level_1_1',
            'spell_slots_used_level_1_2', 'spell_slots_used_level_1_3',
            'spell_slots_used_level_1_4', 'spell_slots_used_level_2_1',
            'spell_slots_used_level_2_2', 'spell_slots_used_level_2_3',
            'spell_slots_used_level_3_1', 'spell_slots_used_level_3_2',
            'spell_slots_used_level_3_3', 'spell_slots_used_level_4_1',
            'spell_slots_used_level_4_2', 'spell_slots_used_level_4_3',
            'spell_slots_used_level_5_1', 'spell_slots_used_level_5_2',
            'spell_slots_used_level_5_3', 'spell_slots_used_level_6_1',
            'spell_slots_used_level_6_2', 'spell_slots_used_level_7_1',
            'spell_slots_used_level_7_2', 'spell_slots_used_level_8_1',
            'spell_slots_used_level_9_1', 'spell_level_1', 'spell_name_1',
            'spell_casting_time_1', 'spell_range_1', 'spell_concentration_1',
            'spell_ritual_1', 'spell_material_required_1', 'spell_notes_1',
            'spell_level_2', 'spell_name_2',
            'spell_casting_time_2', 'spell_range_2', 'spell_concentration_2',
            'spell_ritual_2', 'spell_material_required_2', 'spell_notes_2',
            'spell_level_3', 'spell_name_3',
            'spell_casting_time_3', 'spell_range_3', 'spell_concentration_3',
            'spell_ritual_3', 'spell_material_required_3', 'spell_notes_3',
            'spell_level_4', 'spell_name_4',
            'spell_casting_time_4', 'spell_range_4', 'spell_concentration_4',
            'spell_ritual_4', 'spell_material_required_4', 'spell_notes_4',
            'spell_level_5', 'spell_name_5',
            'spell_casting_time_5', 'spell_range_5', 'spell_concentration_5',
            'spell_ritual_5', 'spell_material_required_5', 'spell_notes_5',
            'appearance_area',
            'backstory_personality', 'alignment', 'languages', 'equipment',
            'magic_attunement_1', 'magic_attunement_1_name',
            'magic_attunement_2', 'magic_attunement_2_name',
            'magic_attunement_3', 'magic_attunement_3_name', 'cp', 'sp', 'ep',
            'gp', 'pp',
        ]

    class_image = forms.ChoiceField(choices=Character.CLASS_IMAGE_CHOICES,
                                    widget=forms.RadioSelect, required=False)
