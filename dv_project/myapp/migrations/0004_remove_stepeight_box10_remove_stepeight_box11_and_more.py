# Generated by Django 4.1.1 on 2022-10-07 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_stepseven_stepeight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stepeight',
            name='box10',
        ),
        migrations.RemoveField(
            model_name='stepeight',
            name='box11',
        ),
        migrations.RemoveField(
            model_name='stepeight',
            name='box8',
        ),
        migrations.RemoveField(
            model_name='stepeight',
            name='box9',
        ),
    ]