from django.shortcuts import render, get_object_or_404
from .models import EducationModel


def education_content(request):
    education_data = EducationModel.objects.all()
    context = {
        'education_data': education_data
    }
    return render(request, 'education_list.html', context)


def education_content_detail(request, ed_item_id):
    education_item = get_object_or_404(EducationModel, pk=ed_item_id)
    context = {
        'education_item': education_item
    }
    return render(request, 'education_detail.html', context)
