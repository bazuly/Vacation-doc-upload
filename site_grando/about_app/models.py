from django.db import models


class AboutEmployeeModel(models.Model):
    name = models.CharField(max_length=128)
    content = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='about/%Y/%m/%d/')
    
    def __str__(self):
        return self.name
    
    
class JobModel(models.Model):
    job_title = models.CharField(max_length=128, null=False)
    
    def __str__(self):
        return self.job_title


class ReferenceBookModel(models.Model):
    name = models.CharField(max_length=128)
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    additional_number = models.IntegerField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True, max_length=512)
    
    def __str__(self):
        return self.name
