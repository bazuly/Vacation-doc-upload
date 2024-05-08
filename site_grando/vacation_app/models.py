from django.db import models


class VacationModel(models.Model):
    name = models.CharField(max_length=128, null=False)
    # добавить календарь
    vacation_date_start = models.CharField(max_length=128)
    vacation_date_end = models.CharField(max_length=128)
    vacation_file = models.FileField(null=False, upload_to='vacation_file_scan/%Y/%m/%d')
    # лицо для согласования???
    # status_confirm = models.BooleanField()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name