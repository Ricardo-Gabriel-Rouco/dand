# Generated by Django 5.1 on 2024-08-29 01:04

import api.validations
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_characters_tokens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='armor_class',
            field=models.IntegerField(default=10, validators=[api.validations.validateArmorClass]),
        ),
        migrations.AlterField(
            model_name='characters',
            name='tokens',
            field=models.IntegerField(blank=True, default=3, null=True),
        ),
    ]
