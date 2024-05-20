from django.urls import path
from .views import * 

urlpatterns = [
    path('news_list', news_list, name='news_list'),
    path('news/news_create', news_create, name='news_create'),
    path('news/news_details/<int:news_id>', news_details, name='news_details'),
    path('news/news_details/<int:news_id>/news_edit', news_edit, name='news_edit')
]
