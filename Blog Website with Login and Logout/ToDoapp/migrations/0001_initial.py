# Generated by Django 2.2.6 on 2019-10-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Retrivedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('task_description', models.CharField(max_length=100)),
                ('task_startdate', models.DateTimeField(max_length=100)),
                ('task_enddate', models.DateTimeField(max_length=100)),
                ('No_of_hours', models.IntegerField()),
                ('priority', models.CharField(max_length=100)),
                ('task_creationdate', models.DateTimeField(max_length=100)),
                ('task_updatedate', models.DateTimeField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tododata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]