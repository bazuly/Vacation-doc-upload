# Generated by Django 5.0.4 on 2024-06-02 14:05

import news_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=news_app.models.upload_to),
        ),
    ]
