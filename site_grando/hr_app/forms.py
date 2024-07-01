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
<<<<<<< HEAD
   # vacancy = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

=======
>>>>>>> 3f83e1c51c79ad783675d46b22669c89a84df671
    class Meta:
        model = VacancyRequestModel
        fields = [
            'name',
            'contact',
            'resume_upload',
<<<<<<< HEAD
            # 'vacancy'
=======
            'covering_letter'
>>>>>>> 3f83e1c51c79ad783675d46b22669c89a84df671
        ]
        labels = {
            'name': 'ФИО',
            'contact': 'Контактная информация для связи с Вами',
            'resume_upload': 'Файл с Вашим резюме',
<<<<<<< HEAD
            #  'vacancy': 'Название вакансии'
=======
            'covering_letter': 'Сопроводительное письмо'
>>>>>>> 3f83e1c51c79ad783675d46b22669c89a84df671
        }
