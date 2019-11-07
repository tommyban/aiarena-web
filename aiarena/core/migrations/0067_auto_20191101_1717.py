# Generated by Django 2.1.7 on 2019-11-01 06:47

from django.db import migrations


def update_user_type(apps, schema_editor):
    # assign types for existing production user accounts
    User = apps.get_model('core', 'User')
    for user in User.objects.filter(service_account=True):
        if user.username == 'stream':
            user.type = 'SERVICE'
        else:
            user.type = 'ARENA_CLIENT'
        user.save()


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0066_auto_20191101_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_type',
            new_name='type',
        ),
        migrations.RunPython(update_user_type),
        migrations.RemoveField(
            model_name='user',
            name='service_account',
        ),
    ]