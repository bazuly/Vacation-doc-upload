from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    