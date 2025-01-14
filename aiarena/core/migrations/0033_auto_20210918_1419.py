# Generated by Django 3.0.14 on 2021-09-18 04:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20210714_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='n_divisions',
            field=models.IntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='competition',
            name='n_placements',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='competition',
            name='rounds_per_cyle',
            field=models.IntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='competition',
            name='rounds_this_cyle',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='competition',
            name='target_division_size',
            field=models.IntegerField(blank=True, default=2, validators=[django.core.validators.MinValueValidator(2)]),
        ),
        migrations.AddField(
            model_name='competition',
            name='target_n_divisions',
            field=models.IntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='competitionparticipation',
            name='division_num',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
