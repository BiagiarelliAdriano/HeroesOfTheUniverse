# Generated by Django 4.2.16 on 2024-11-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0003_rename_class_features_character_class_features_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='damage_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='weapon_notes',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
