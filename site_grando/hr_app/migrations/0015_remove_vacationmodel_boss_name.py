# Generated by Django 5.0.4 on 2024-07-08 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0014_alter_vacationmodel_boss_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacationmodel',
            name='boss_name',
        ),
    ]
