# Generated by Django 3.0.8 on 2020-09-22 10:50

from django.db import migrations

from aiarena.core.models import ArenaClient


def migrate_arenaclient_users(apps, schema_editor):
    User = apps.get_model('core', 'User')
    ac_users = User.objects.filter(type='ARENA_CLIENT')

    for ac_user in ac_users:
        # find parent class fields:
        fields = [f.name for f in User._meta.fields]

        # get the values from the user instance
        values = dict([(x, getattr(ac_user, x)) for x in fields])

        # assign same values to new instance of second model
        new_instance = ArenaClient(**values)
        new_instance.trusted = True
        new_instance.owner = User.objects.get(id=1)  # owner field will be removed, assign to superuser
        new_instance.save()  # save new one

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0114_arenaclientstatus'),
    ]

    operations = [
        migrations.RunPython(migrate_arenaclient_users),
    ]
