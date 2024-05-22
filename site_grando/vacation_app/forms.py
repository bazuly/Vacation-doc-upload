from django import forms
from .models import VacationModel


class VacationForm(forms.ModelForm):
    class Meta:
        model = VacationModel
        fields = ['name', 'vacation_date_start', 'vacation_date_end', 'status_confirm']

        labels = {
            'name': 'ФИО',
            'vacation_date_start': 'Дата начала отпуска',
            'vacation_date_end': 'Дата окончания отпуска',
        }

    def __init__(self, *args, **kwargs):
        super(VacationForm, self).__init__(*args, **kwargs)
        self.fields['status_confirm'].widget = forms.HiddenInput()