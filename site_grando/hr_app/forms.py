from django import forms
from .models import VacationModel, VacancyModel, VacancyRequestModel


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
            # 'boss_name'
        ]
        labels = {
            'name': 'ФИО',
            'vacation_date_start': 'Дата начала отпуска',
            'vacation_date_end': 'Дата окончания отпуска',
            'job': 'Должность',
            'vacation_type': 'Вариант отпуска',
            # 'boss_name': 'Кому'

        }
        widgets = {
            'vacation_date_start': forms.DateInput(attrs={'id': 'id_vacation_date_start', 'type': 'text'}),
            'vacation_date_end': forms.DateInput(attrs={'id': 'id_vacation_date_end', 'type': 'text'}),
        }


    def __init__(self, *args, **kwargs):
        super(VacationForm, self).__init__(*args, **kwargs)
        self.fields['status_confirm'].widget = forms.HiddenInput()
        self.fields['status_confirm'].initial = 'На согласовании'


class VacancyForm(forms.ModelForm):
    class Meta:
        model = VacancyModel
        fields = [
            'vacancy_name',
            'salary',
            'content'
        ]
        labels = {
            'vacancy_name': 'Название вакансии',
            'salary': 'Оклад',
            'content': 'Содержание'
        }


class VacancyRequestForm(forms.ModelForm):
   # vacancy = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = VacancyRequestModel
        fields = [
            'name',
            'contact',
            'resume_upload',
            # 'vacancy'
        ]
        labels = {
            'name': 'ФИО',
            'contact': 'Контактная информация для связи с Вами',
            'resume_upload': 'Файл с Вашим резюме',
            #  'vacancy': 'Название вакансии'
        }
