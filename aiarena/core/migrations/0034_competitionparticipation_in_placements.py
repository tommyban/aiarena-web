# Generated by Django 3.0.14 on 2021-09-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20210918_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitionparticipation',
            name='in_placements',
            field=models.BooleanField(default=True),
        ),
    ]
