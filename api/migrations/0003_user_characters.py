# Generated by Django 5.0.7 on 2024-07-19 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_dm_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='characters',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.characters'),
        ),
    ]
