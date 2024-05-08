from django.shortcuts import render
from .forms import VacationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import VacationModel
from django.core.mail import EmailMessage


def vacation_upload_success(request):
    return render(request, 'vacation_upload_success.html')


def send_email_to_hr(name, vacation_date_start, vacation_date_end, vacation_file_path):
    to_email = ['serejka50@gmail.com']
    subject = f'Заявление на отпуск от {name}'
    message = f'Прошу предоставить отпуск в период с {vacation_date_start} по {vacation_date_end}'
    email = EmailMessage(subject, message, to=to_email)
    email.attach_file(vacation_file_path)
    email.send()


def vacation_upload(request):
    if request.method == 'POST':
        vac_form = VacationForm(
            request.POST,
            request.FILES,
            prefix='vac'
        )
        if vac_form.is_valid():
            vac_data = VacationModel(
                name = vac_form.cleaned_data['name'],
                vacation_date_start = vac_form.cleaned_data['vacation_date_start'],
                vacation_date_end = vac_form.cleaned_data['vacation_date_end'],
                vacation_file = request.FILES.get('vacation_file')
            )
            
            vac_data.save()
            print('Vacation data saved successfully')
            
            vacation_file_path = vac_data.vacation_file.path
            
            send_email_to_hr(
                vac_data.name,
                vac_data.vacation_date_start,
                vac_data.vacation_date_end,
                vacation_file_path
            )
            
            return HttpResponseRedirect(reverse('vacation_app:vacation_upload_success'))

        else:
            return print('Vacatioon_data_upload form is not valid', vac_form.errors)
    
    else:
        vac_form = VacationForm(prefix='vac')
    
    return render(request, 'vacation_upload.html', {'vac_form': vac_form})


