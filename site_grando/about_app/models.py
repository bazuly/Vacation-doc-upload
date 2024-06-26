from django.db import models
import os 


def upload_to(instance, filename):
    return os.path.join('about', instance.name, filename)


class AboutEmployeeModel(models.Model):
    name = models.CharField(max_length=128)
    content = models.CharField(max_length=256)
    photo = models.ImageField(upload_to=upload_to)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    
class JobModel(models.Model):
    job_title = models.CharField(max_length=128, null=False)
    
    def save(self, *args, **kwargs):
        self.job_title = self.job_title.lower()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.job_title


class WorkPlace(models.Model):
    work_place = models.CharField(max_length=128, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.work_place = self.work_place.lower()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.work_place
    

class ReferenceBookModel(models.Model):
    name = models.CharField(max_length=128)
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    additional_number = models.IntegerField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True, max_length=512)
    work_place = models.ForeignKey(WorkPlace, on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        if self.additional_info:
            self.additional_info = self.additional_info.lower()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
