from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class EducationModel(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Название',
        null=False,
    )
    content = RichTextUploadingField()
    uploaded_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title
