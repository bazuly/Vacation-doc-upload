# Generated by Django 5.0.4 on 2024-06-25 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0005_alter_vacancymodel_short_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancymodel',
            old_name='short_description',
            new_name='Краткое описание',
        ),
    ]
