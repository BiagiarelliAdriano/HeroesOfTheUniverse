# Generated by Django 4.2.16 on 2024-11-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0002_character_weapon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='class_features',
            new_name='class_features_1',
        ),
        migrations.AddField(
            model_name='character',
            name='class_features_2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
