from django.shortcuts import render
from .models import AboutEmployeeModel, ReferenceBookModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import ReferenceBookModel


def index_about(request):
    data = AboutEmployeeModel.objects.all()
    return render(request, 'list_about_major_employer.html', {'data': data})


""" CONTACT EMPOLYERS DATA VIEW """


@login_required
def reference_book_list(request):
    reference_book_data_list = ReferenceBookModel.objects.all()
    item_per_page = 10
    paginator = Paginator(reference_book_data_list, item_per_page)
    page = request.GET.get('page')
    try:
        reference_book_data = paginator.page(page)
    except PageNotAnInteger:
        reference_book_data = paginator.page(1)
    except EmptyPage:
        reference_book_data = paginator.page(paginator.num_pages)
    
    context = {
        'reference_book_data': reference_book_data
    }
    return render(request, 'list_reference_book.html', context)


@login_required
def search_data_reference_book(request):
    query = request.GET.get('q').strip()
    query_lower = query.lower()
    vac_data = ReferenceBookModel.objects.all()

    if query:
        vac_data = ReferenceBookModel.objects.filter(
            Q(name__icontains=query_lower) |
            Q(job__icontains=query_lower) |
            Q(additional_number__icontains=query_lower)
        )
    else:
        query = vac_data

    context = {
        'vac_data': vac_data,
        'query': query
    }

    return render(request, 'list_vacation.html', context)