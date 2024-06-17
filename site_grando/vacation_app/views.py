from django.shortcuts import render, get_object_or_404
from .forms import VacationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import VacationModel
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from .models import HrEmailModel


""" Success redirections """


def vacation_upload_success(request):
    return render(request, 'vacation_upload_success.html')


def vacation_edit_success(request):
    return render(request, 'vacation_edit_success.html')


""" List all vacations requests """


def list_vac(request):
    vac_data = VacationModel.objects.all().order_by('-uploaded_at')

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


""" Edit status: In process, Approved, Declined """


@login_required
@permission_required('vacation_app.can_edit_vacation_status')
def edit_vacation_status(request, vacation_id):
    vacation = get_object_or_404(VacationModel, pk=vacation_id)
    if request.method == 'POST':
        status_confirm = request.POST.get('status_confirm')
        vacation.status_confirm = status_confirm
        vacation.save()
        return HttpResponseRedirect(reverse('vacation_app:vacation_edit_success'))
    else:
        return render(request, 'edit_vacation_status.html', {'vacation': vacation})


""" Email sending """


def send_email_to_hr(name, vacation_date_start, vacation_date_end, vacation_file_path, job_title):
    hr_email_instance = HrEmailModel.objects.all()
    email_list = [email.email for email in hr_email_instance]
    subject = f'Заявление на отпуск от {name}, должность: {job_title}'
    message = f'Прошу предоставить отпуск в период с {vacation_date_start} по {vacation_date_end}'
    email = EmailMessage(subject, message, to=email_list)
    email.attach_file(vacation_file_path)
    email.send()


""" Upload vacation data """

def vacation_upload(request):
    if request.method == 'POST':
        vac_form = VacationForm(request.POST, request.FILES, prefix='vac')
        if vac_form.is_valid():
            vac_data = vac_form.save(commit=False)
            vac_data.vacation_file = request.FILES.get('vacation_file')
            vac_data.status_confirm = 'На согласовании'
            vac_data.save()

            vacation_file_path = vac_data.vacation_file.path

            send_email_to_hr(
                vac_data.name,
                vac_data.vacation_date_start,
                vac_data.vacation_date_end,
                vacation_file_path,
                vac_data.job.job_title,
            )

            return HttpResponseRedirect(reverse('vacation_app:vacation_upload_success'))
        else:
            print('Vacation_data_upload form is not valid', vac_form.errors)
            return render(request, 'vacation_upload.html', {'vac_form': vac_form})
    else:
        vac_form = VacationForm(prefix='vac')
    return render(request, 'vacation_upload.html', {'vac_form': vac_form})


"""SEARCH VACATION DATA AUTH USER"""


def search_vac_data(request):
    query = request.GET.get('q', '').strip()
    query_lower = query.lower()
    vac_data = VacationModel.objects.all()

    if query:
        vac_data = VacationModel.objects.filter(
            Q(name__icontains=query_lower)
        )
    else:
        query = vac_data

    context = {
        'vac_data': vac_data,
        'query': query
    }

    return render(request, 'list_vacation.html', context)


"""SEARCH VACATION DATA NOT AUTH USER"""


def non_auth_vacation_search(request):
    query = request.GET.get('q', '').strip()
    query_lower = query.lower()
    vac_data = ''

    if query:
        vac_data = VacationModel.objects.filter(
            Q(name__icontains=query_lower)
        )
    else:
        query = vac_data

    context = {
        'vac_data': vac_data,
        'query': query
    }

    return render(request, 'non_auth_search_vac.html', context)