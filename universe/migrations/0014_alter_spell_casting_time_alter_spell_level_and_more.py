# Generated by Django 4.2.16 on 2024-12-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0013_alter_weapon_attack_bonus_save_dc_alter_weapon_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='casting_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='level',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='spell_range',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
