# Generated by Django 5.0.4 on 2024-06-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacation_app', '0002_alter_vacationmodel_vacation_date_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationmodel',
            name='vacation_file',
            field=models.FileField(blank=True, null=True, upload_to='vacation_file_scan/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='vacationmodel',
            name='vacation_type',
            field=models.CharField(choices=[('Оплачиваемый отпуск', 'Оплачиваемый отпуск'), ('За счет сотрудника', 'За счет сотрудника')], default=('Оплачиваемый отпуск', 'Оплачиваемый отпуск'), max_length=128),
        ),
    ]
