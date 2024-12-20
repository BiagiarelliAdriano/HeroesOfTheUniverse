# Generated by Django 4.2.16 on 2024-12-12 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0010_character_alignment_character_appearance_area_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('casting_time', models.CharField(max_length=100)),
                ('spell_range', models.CharField(max_length=100)),
                ('concentration', models.BooleanField(default=False)),
                ('ritual', models.BooleanField(default=False)),
                ('material_required', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, null=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spells', to='universe.character')),
            ],
        ),
    ]
