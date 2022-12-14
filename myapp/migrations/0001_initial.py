# Generated by Django 4.1.1 on 2022-09-25 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StepTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box1', models.CharField(max_length=100, null=True)),
                ('box2', models.CharField(max_length=100, null=True)),
                ('box3', models.CharField(max_length=100, null=True)),
                ('box4', models.CharField(max_length=100, null=True)),
                ('box5', models.CharField(max_length=100, null=True)),
                ('box6', models.CharField(max_length=100, null=True)),
                ('box7', models.CharField(max_length=100, null=True)),
                ('box8', models.CharField(max_length=100, null=True)),
                ('box9', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StepThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box1', models.CharField(max_length=100, null=True)),
                ('box2', models.CharField(max_length=100, null=True)),
                ('box3', models.CharField(max_length=100, null=True)),
                ('box4', models.CharField(max_length=100, null=True)),
                ('box5', models.CharField(max_length=100, null=True)),
                ('box6', models.CharField(max_length=100, null=True)),
                ('box7', models.CharField(max_length=100, null=True)),
                ('box8', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StepOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box1', models.CharField(max_length=100, null=True)),
                ('box2', models.CharField(max_length=100, null=True)),
                ('box3', models.CharField(max_length=100, null=True)),
                ('box4', models.CharField(max_length=100, null=True)),
                ('box5', models.CharField(max_length=100, null=True)),
                ('box6', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StepFour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box1', models.CharField(max_length=100, null=True)),
                ('box2', models.CharField(max_length=100, null=True)),
                ('box3', models.CharField(max_length=100, null=True)),
                ('box4', models.CharField(max_length=100, null=True)),
                ('box5', models.CharField(max_length=100, null=True)),
                ('box6', models.CharField(max_length=100, null=True)),
                ('box7', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StepFive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box1', models.CharField(max_length=100, null=True)),
                ('box2', models.CharField(max_length=100, null=True)),
                ('box3', models.CharField(max_length=100, null=True)),
                ('box4', models.CharField(max_length=100, null=True)),
                ('box5', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
