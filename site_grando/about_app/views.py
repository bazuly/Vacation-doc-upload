from django.shortcuts import render
from .models import AboutEmployeeModel, ReferenceBookModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import ReferenceBookModel
from site_grando.handlers.pagination_handler import paginate_queryset


def index_about(request):
    data = AboutEmployeeModel.objects.all()
    return render(request, 'list_about_major_employer.html', {'data': data})


""" CONTACT EMPOLYERS DATA VIEW """


@login_required
def reference_book_list(request):
    reference_book_data_list = ReferenceBookModel.objects.all()
    reference_book_data_paginate = paginate_queryset(
        reference_book_data_list,
        request
    )
    context = {
        'reference_book_data': reference_book_data_paginate
    }
    return render(request, 'list_reference_book.html', context)


@login_required
def search_data_reference_book(request):
    query = request.GET.get('q').strip()
    query_lower = query.lower()
    reference_book_data = ReferenceBookModel.objects.all()

    if query:
        reference_book_data = ReferenceBookModel.objects.filter(
            Q(name__icontains=query_lower) |
            Q(job__job_title__icontains=query_lower) |
            Q(additional_number__icontains=query_lower) |
            Q(additional_info__icontains=query_lower)
        )
    else:
        query = reference_book_data

    context = {
        'reference_book_data': reference_book_data,
        'query': query
    }

    return render(request, 'list_reference_book.html', context)
