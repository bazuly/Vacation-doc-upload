from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsModel
from .forms import NewsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


""" LIST|ADD NEWS """


def news_list(request):
    news_data = NewsModel.objects.all().order_by('-published_at')
    
    items_per_page = 5
    paginator = Paginator(news_data, items_per_page)
    page = request.GET('page')
    try:
        news_data = paginator.page(page)
    except PageNotAnInteger:
        news_data = paginator.page(1)
    except EmptyPage:
        news_data = paginator.page(paginator.num_pages)
        
    context = {
        'news_data': news_data
    }
    
    return render(request, 'news_list.html', context)


def news_details(request, news_id):
    news_item = get_object_or_404(NewsModel, pk=news_id)
    return render(request, 'news_details.html', {'news_item': news_item})


def news_create(request):
    if request.method == 'POST':
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            news_form.save()
            return redirect('news_list')
    else:
        news_form = NewsForm()
    return render(request, 'news_form.html', {'news_form': news_form})


def news_edit(request, news_id):
    news_item = get_object_or_404(NewsModel, pk=news_id)
    if request.method == 'POST':
        news_form = NewsForm(request.POST, instance=news_item)
        if news_form.is_valid():
            news_form.save()
            return redirect('news_list')
    else:
        news_form = NewsForm(instance=news_item)
    return render(request, 'news_form.html', {'news_form': news_form})