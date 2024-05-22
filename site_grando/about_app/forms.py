from django import forms
from .models import AboutEmployeeModel


class AboutEmployeeForm(forms.ModelForm):
    class Meta:
        model = AboutEmployeeModel
        fields = ['name', 'content', 'photo']