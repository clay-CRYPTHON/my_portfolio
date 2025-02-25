# Generated by Django 5.0.3 on 2024-03-27 13:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceEdu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Ex', 'Experience'), ('ED', 'Education')], max_length=2)),
                ('date', models.DateTimeField(unique_for_year=django.utils.timezone.now)),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SkillsLang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
