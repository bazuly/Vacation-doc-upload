from django.shortcuts import render
from .models import AboutEmployeeModel


def index_about(request):
    data = AboutEmployeeModel.objects.all()
    return render(request, 'list_about_employer.html', {'data': data})