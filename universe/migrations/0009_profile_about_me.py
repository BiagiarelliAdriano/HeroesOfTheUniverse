# Generated by Django 4.2.16 on 2024-12-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0008_alter_character_class_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, null=True),
        ),
    ]