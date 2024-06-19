from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

from vacation_app.handlers.email_handler import email_hr_handler
from .forms import VacationForm
from .models import VacationModel

from datetime import datetime, timedelta


""" Success redirections """


def vacation_upload_success(request):
    return render(request, 'vacation_upload_success.html')


def vacation_edit_success(request):
    return render(request, 'vacation_edit_success.html')


""" Search form for non auth users """

def search_form_non_auth_user(request):
    return render(request, 'non_auth_search_page.html')


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

            email_hr_handler(
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
    vac_data = None

    current_date = datetime.now().date()
    half_year = current_date - timedelta(days=6*30)

    if query:
        vac_data = VacationModel.objects.filter(
            Q(uploaded_at__gte=half_year) &
            Q(name__icontains=query_lower)
        )
    else:
        # Просто верните пустой набор данных, если нет запроса
        vac_data = VacationModel.objects.none()

    context = {
        'vac_data': vac_data,
        'query': query
    }

    return render(request, 'non_auth_search_empl_application.html', context)
