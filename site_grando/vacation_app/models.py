from django.db import models
from about_app.models import JobModel


class VacationModel(models.Model):
    STATUS_CHOICES = [
        ('На согласовании', 'На согласовании'),
        ('Согласовано', 'Согласовано'),
        ('Отказ', 'Отказ')
    ]
    name = models.CharField(max_length=128, null=False)
    uploaded_at = models.DateTimeField(auto_now=True)
    vacation_date_start = models.CharField(max_length=128)
    vacation_date_end = models.CharField(max_length=128)
    vacation_file = models.FileField(null=False,
                                     upload_to='vacation_file_scan/%Y/%m/%d')
    status_confirm = models.CharField(max_length=128,
                                      choices=STATUS_CHOICES,
                                      default=STATUS_CHOICES[0])
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class HrEmailModel(models.Model):
    email = models.EmailField(max_length=128, null=False)
    
    def __str__(self):
        return self.email