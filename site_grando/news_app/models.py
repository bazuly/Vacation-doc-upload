from django.db import models
import os
from ckeditor.fields import RichTextField


def upload_to(instance, filename):
    return os.path.join('news', instance.title, filename)


class NewsModel(models.Model):
    title = models.CharField(max_length=256)
    content = RichTextField()
    published_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to=upload_to, null=True, blank=True)
  #  context_photo = models.ImageField(upload_to=upload_to, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


""" Добавить также возможность добавления контекстных фото в статье через ckeditor """
""" + разобраться с версией, а то что-то джанга ругается чуть """