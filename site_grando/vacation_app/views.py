from django.shortcuts import render, get_object_or_404
from .forms import VacationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import VacationModel
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def vacation_upload_success(request):
    return render(request, 'vacation_upload_success.html')

def vacation_edit_success(request):
    return render(request, 'vacation_edit_success.html')


def list_vac(request):
    vac_data = VacationModel.objects.all()

    item_per_page = 7
    paginator = Paginator(vac_data, item_per_page)
    page = request.GET.get('page')
    try:
        vac_data = paginator.page(page)
    except PageNotAnInteger:
        vac_data = paginator.page(1)
    except EmptyPage:
        vac_data = paginator.page(paginator.num_pages)
    context = {
        'vac_data': vac_data
    }

    return render(request, 'list_vacation.html', context)

def edit_vacation_status(request, vacation_id):
    vacation = get_object_or_404(VacationModel, pk=vacation_id)
    if request.method == 'POST':
        status_confirm = request.POST.get('status_confirm')
        vacation.status_confirm = status_confirm
        vacation.save()
        return HttpResponseRedirect(reverse('vacation_app:vacation_edit_success'))
    else:
        return render(request, 'edit_vacation_status.html', {'vacation': vacation})


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
                name=vac_form.cleaned_data['name'],
                vacation_date_start=vac_form.cleaned_data['vacation_date_start'],
                vacation_date_end=vac_form.cleaned_data['vacation_date_end'],
                vacation_file=request.FILES.get('vacation_file'),
                status_confirm=vac_form.cleaned_data['status_confirm']
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
            return print('Vacation_data_upload form is not valid', vac_form.errors)

    else:
        vac_form = VacationForm(prefix='vac')

    return render(request, 'vacation_upload.html', {'vac_form': vac_form})

