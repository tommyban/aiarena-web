# Generated by Django 2.1.7 on 2019-10-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_round_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='number',
            field=models.IntegerField(blank=True),
            preserve_default=False,
        ),
    ]