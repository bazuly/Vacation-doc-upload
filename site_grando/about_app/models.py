from django.db import models


class AboutEmployeeModel(models.Model):
    name = models.CharField(max_length=128)
    content = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='about/%Y/%m/%d/')
    
    def __str__(self):
        return self.name
    