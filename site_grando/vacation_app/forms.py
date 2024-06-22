from django import forms
from .models import VacationModel


class VacationForm(forms.ModelForm):
    class Meta:
        model = VacationModel
        fields = [
            'name',
            'vacation_date_start',
            'vacation_date_end',
            'status_confirm',
            'job',
            'vacation_type',
            'boss_name'
        ]
        labels = {
            'name': 'ФИО',
            'vacation_date_start': 'Дата начала отпуска',
            'vacation_date_end': 'Дата окончания отпуска',
            'job': 'Должность',
            'vacation_type': 'Вариант отпуска',
            'boss_name': 'Кому'
            
        }
    
    def __init__(self, *args, **kwargs):
        super(VacationForm, self).__init__(*args, **kwargs)
        self.fields['status_confirm'].widget = forms.HiddenInput()
        self.fields['status_confirm'].initial = 'На согласовании'