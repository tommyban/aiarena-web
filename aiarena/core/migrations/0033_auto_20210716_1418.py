# Generated by Django 3.0.14 on 2021-07-16 04:48

from django.db import migrations

from aiarena.core.models import User, ServiceUser


def migrate_service_users(apps, schema_editor):
    pass  # migration was broken - moved to new migration.


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0032_auto_20210714_2351'),
    ]

    operations = [
        migrations.RunPython(migrate_service_users),
    ]
