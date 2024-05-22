# Generated by Django 5.0.4 on 2024-05-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutEmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=256)),
                ('photo', models.ImageField(upload_to='about/%Y/%m/%d/')),
            ],
        ),
    ]