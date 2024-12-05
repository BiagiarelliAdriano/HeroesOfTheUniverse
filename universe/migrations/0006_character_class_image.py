# Generated by Django 4.2.16 on 2024-12-02 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0005_alter_weapon_weapon_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='class_image',
            field=models.CharField(choices=[('barbarian', 'Barbarian'), ('bard', 'Bard'), ('cleric', 'Cleric'), ('druid', 'Druid'), ('fighter', 'fighter'), ('monk', 'Monk'), ('paladin', 'Paladin'), ('ranger', 'Ranger'), ('rogue', 'Rogue'), ('sorcerer', 'Sorcerer'), ('warlock', 'Warlock'), ('wizard', 'Wizard')], default='barbarian', max_length=50),
        ),
    ]