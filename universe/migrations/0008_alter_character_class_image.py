# Generated by Django 4.2.16 on 2024-12-03 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0007_alter_character_class_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='class_image',
            field=models.CharField(blank=True, choices=[('barbarian', 'Barbarian'), ('bard', 'Bard'), ('cleric', 'Cleric'), ('druid', 'Druid'), ('fighter', 'Fighter'), ('monk', 'Monk'), ('paladin', 'Paladin'), ('ranger', 'Ranger'), ('rogue', 'Rogue'), ('sorcerer', 'Sorcerer'), ('warlock', 'Warlock'), ('wizard', 'Wizard')], default='barbarian', max_length=50, null=True),
        ),
    ]