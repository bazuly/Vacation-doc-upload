from django.urls import path 
from .views import index_about


app_name = 'about_app'

urlpatterns = [
    path('page_about', index_about, name='page_about')
]

