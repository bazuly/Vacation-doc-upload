from django.shortcuts import render
from .models import AboutEmployeeModel, ReferenceBookModel


def index_about(request):
    data = AboutEmployeeModel.objects.all()
    return render(request, 'list_about_major_employer.html', {'data': data})


""" CONTACT EMPOLYERS DATA VIEW """


def reference_book_list(requset):
    reference_book_data_list = ReferenceBookModel.objects.all()
    context = {
        'reference_book_data_list': reference_book_data_list
    }
    return render(requset, 'list_reference_book.html', context)


def search_data_reference_book(request):
    pass 