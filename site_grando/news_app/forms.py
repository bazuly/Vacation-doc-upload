from django import forms 
from .models import NewsModel
from ckeditor.widgets import CKEditorWidget


class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = NewsModel
        fields = ['title', 'content']
    
        labels = {
            'title': 'Заголовок',
            'content': 'Текст'
        }