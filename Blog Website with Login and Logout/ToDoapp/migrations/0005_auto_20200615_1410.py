# Generated by Django 2.2.7 on 2020-06-15 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoapp', '0004_auto_20200615_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tododata',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tododata',
            old_name='passwordo',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='tododata',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='tododata',
            name='passwordt',
        ),
        migrations.RemoveField(
            model_name='tododata',
            name='username',
        ),
    ]
