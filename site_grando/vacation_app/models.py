from django.db import models


class VacationModel(models.Model):
    STATUS_CHOICES = [
        ('На согласовании', 'На согласовании'),
        ('Согласовано', 'Согласовано'),
        ('Отказ', 'Отказ')
    ]
    name = models.CharField(max_length=128, null=False)
    vacation_date_start = models.CharField(max_length=128)
    vacation_date_end = models.CharField(max_length=128)
    vacation_file = models.FileField(null=False, upload_to='vacation_file_scan/%Y/%m/%d')
    status_confirm = models.CharField(max_length=128, choices=STATUS_CHOICES, default=STATUS_CHOICES[0])
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
